from django.contrib import admin
from django.urls import path, include

from core.views import LoginView, LogoutView

from django.contrib.auth.decorators import permission_required
from django.contrib.admin.views.decorators import staff_member_required

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('game_api.urls', namespace='game')),
    path('api/', include('trivia_api.urls', namespace='trivia')),
    path('api/', include('core.urls')),
    path('api/auth/', include('auth_api.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # permissions login required
    # https://django.fun/en/qa/421446/
    # path('api/docs/', permission_required('is_staff', login_url='core:login')(SpectacularSwaggerView.as_view(url_name='schema')), name='docs')
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs')
]
