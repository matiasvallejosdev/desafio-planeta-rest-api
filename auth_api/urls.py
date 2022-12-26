from django.urls import include, path
from auth_api import views

app_name = 'auth_api'
urlpatterns = [
    path('', views.UserConnectionAPI.as_view(), name='connection'),
    path('create/', views.UserCreateView.as_view(), name='create'),
    path('token/', views.UserTokenAPI.as_view(), name='token'),
    path('me/', views.UserManageView.as_view(), name='me'),
]