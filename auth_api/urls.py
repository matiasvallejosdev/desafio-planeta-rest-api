from django.urls import include, path
from auth_api import views

app_label = 'auth_api'
urlpatterns = [
    path('', views.TestConnectionAPI.as_view(), name='test-connection'),
    path('user/create/', views.UserCreateAPI.as_view(), name='create_user'),
    path('user/<int:pk>/', views.UserRetrieveAPI.as_view(), name='retrieve_user'),
    path('token/', views.UserTokenAPI.as_view(), name='token'),
]
