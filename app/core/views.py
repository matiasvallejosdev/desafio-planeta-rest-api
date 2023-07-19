from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import reverse_lazy

from .forms import LoginForm


class UserLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    # Change authentication form
    # https://stackoverflow.com/questions/61033328/how-to-change-a-label-of-authenticationform-called-in-the-loginview-and-how-to-u
    authentication_form = LoginForm

    def __init__(self, *args, **kwargs):
        super(UserLoginView, self).__init__(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('docs')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('core:login')
