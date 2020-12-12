from django.urls import include, path

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'task', views.TaskModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api_login', views.user_login),
    path('user_list/', views.UserList.as_view(), name='user_list'),
    path('user_create/', views.UserCreate.as_view(), name='user_create'),
    path('user_retrieve_update_destroy/<int:pk>',
         views.UserRetrieveUpdateDestroy.as_view(),
         name='user_retrieve_update_destroy'),
]
