from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.http import require_POST

from .forms import UserUpdateForm, ProfileUpdateForm

from core.common.decorators import ajax_required


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('auth:login')
    template_name = 'signup.html'

@ajax_required
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
    return render(request, 'registration/login.html')    

@login_required
def settings(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(data=request.POST) 
        profile_form = ProfileUpdateForm()
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserUpdateForm(instance=request.user, data=request.POST) 
        profile_form = ProfileUpdateForm(instance=request.user.profile, data=request.POST)

    return render(request, 'auth/settings.html', {'user_form': user_form, 'profile_form': profile_form})