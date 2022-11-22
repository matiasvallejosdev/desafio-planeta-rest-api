from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

from core.views import LoginView, LogoutView

from django.contrib.auth.decorators import permission_required

schema_view = get_swagger_view(title='ClimateChallengeAPI')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('game_api.urls')),
    path('api/core/', include('core.urls')),
    path('api/auth/', include('auth_api.urls')),
    # https://django.fun/en/qa/421446/
    # permissions login required
    path('api/docs/', permission_required('MySpecPermissionForRedoc', login_url="/api/core/login/")(
             get_swagger_view(title='ClimateChallengeAPI')),
         name='docs')
]
