from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from auth_api import serializers, permissions as auth_api_permissions

from django.contrib.auth import get_user_model


class UserConnectionAPI(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return Response({
            "detail": "Connection successfully!"
        })


class UserCreateAPI(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class UserRetrieveAPI(generics.RetrieveAPIView):
    serializer_class = serializers.UserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = (permissions.IsAdminUser,)


class UserListAPI(generics.ListAPIView):
    serializer_class = serializers.UserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = (permissions.IsAdminUser,)


class UserTokenAPI(ObtainAuthToken):
    serializer_class = serializers.AuthSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
