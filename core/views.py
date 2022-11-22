from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import reverse_lazy


class UserLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def __init__(self, *args, **kwargs):
        super(UserLoginView, self).__init__(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('docs')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')
