from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from accounts.models import User
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.db import transaction
from djoser import views
from djoser.conf import settings


class SignUP(TemplateView):
    template_name = 'registration/registration.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        user_form = UserRegistrationForm(request.POST, request.FILES)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_user = authenticate(
                username=user_form.cleaned_data['email'], password=user_form.cleaned_data['password'])
            login(request, new_user)
            return redirect('catalog-index')
        return render(request, self.template_name, {'user_form': user_form})    
    
    
    
    
  