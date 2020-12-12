from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK

from .models import Task, User
from .serializers import UserModelSerializer, TaskModelSerializer

from .permissions import IsOwner


@csrf_exempt
@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def user_login(request):
    """ Function based view function designed to create user token
    Provide correct login+password pair to get the token
    Add "Authorization Token <Token>" header in all subsequent requests
    """
    username = request.data.get('username')
    password = request.data.get('password')

    if username is None or password is None:
        return Response({'error': 'Invalid username or password'})
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid data'})

    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=HTTP_200_OK)


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserModelSerializer(users, many=True)
        return Response(serializer.data)


class UserCreate(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserModelSerializer


class UserRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class TaskModelViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer

    def get_permissions(self):
        """Set custom permissions for each action."""
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsOwner]
        elif self.action in ['list', 'retrieve', 'create']:
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()
