from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .forms import UserUpdateForm, ProfileUpdateForm


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('auth:login')
    template_name = 'signup.html'

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