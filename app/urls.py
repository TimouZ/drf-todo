from django.urls import include, path

from rest_framework import routers

from . import views

# router = routers.SimpleRouter()
# router.register(r'task_list', views.TaskList)

router = routers.SimpleRouter()
router.register(r'task_list', views.TaskModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api_login', views.user_login),
    path('user_list/', views.UserList.as_view(), name='user_list'),
    path('user_create/', views.UserCreate.as_view(), name='user_create'),
    path('user_retrieve_update_destroy/<int:pk>',
         views.UserRetrieveUpdateDestroy.as_view(),
         name='user_retrieve_update_destroy'),
    # path('task_create/', views.TaskCreate.as_view(), name='task_create'),
    # path('task_update/<int:pk>', views.TaskUpdate.as_view(), name='task_update'),
    # path('task_destroy/<int:pk>', views.TaskDestroy.as_view(), name='task_destroy'),
]
