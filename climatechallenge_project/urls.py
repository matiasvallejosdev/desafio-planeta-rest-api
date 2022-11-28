from django.contrib import admin
from django.urls import path, include

from core.views import LoginView, LogoutView

from rest_framework_swagger.views import get_swagger_view
from django.contrib.auth.decorators import permission_required
from django.contrib.admin.views.decorators import staff_member_required

schema_view = get_swagger_view(title='ClimateChallengeAPI')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('game_api.urls', namespace='game')),
    path('api/', include('trivia_api.urls', namespace='trivia')),
    path('api/', include('core.urls')),
    path('api/auth/', include('auth_api.urls')),
    # permissions login required
    # https://django.fun/en/qa/421446/
    path('api/docs/', permission_required('is_staff', login_url='core:login')(
             get_swagger_view(title='ClimateChallengeAPI')),
         name='docs')
]
