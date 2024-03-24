from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from . forms import UserCreationForm
from . models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# from . utils import send_verification_code


class UserRegisterView(LoginRequiredMixin, View):
    form = UserCreationForm

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        pass

