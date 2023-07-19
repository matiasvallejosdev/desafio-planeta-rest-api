from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('core.urls')),
    path('api/game/', include('game_api.urls', namespace='game')),
    path('api/trivia/', include('trivia_api.urls', namespace='trivia')),
    path('api/player/', include('player_api.urls', namespace='player')),

    path("api/rest/auth/", include("dj_rest_auth.urls"), name='rest-auth'),  # endpoints provided by dj-rest-auth
    path('api/auth/', include('auth_api.urls'), name='auth'),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs')
]
