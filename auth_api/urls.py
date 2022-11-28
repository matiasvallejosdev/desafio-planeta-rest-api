from django.urls import include, path
from auth_api import views

app_label = 'auth_api'
urlpatterns = [
    path('user/create/', views.UserCreateAPI.as_view(), name='create_user'),
    path('user/<int:pk>/', views.UserRetrieveAPI.as_view(), name='retrieve_user'),
    path('user/', views.UserListAPI.as_view(), name='list_user'),
    path('token/', views.UserTokenAPI.as_view(), name='token'),
]
