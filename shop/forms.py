from dataclasses import field
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import agents
from .models import clients
from .models import plots
from .models import blogs
from .models import stats

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields={'username','email','password1','password2'}

class agentForm(forms.ModelForm):
 class Meta:
  model = agents
  fields = '__all__'
  labels = {'photo':'', 'name':'Name'}

class clientForm(forms.ModelForm):
    class Meta:
        model=clients
        fields = '__all__'
        labels = {'name':'Name', 'photo':'', 'type':'Type', 'description':'Description'}

class blogForm(forms.ModelForm):
    class Meta:
        model = blogs
        fields = '__all__'
        labels = {'name':'Name', 'photo':'', 'date':'date', 'description':'Description'}

class plotForm(forms.ModelForm):
    class Meta:
        model = plots
        fields = '__all__'
        labels = {'description':'Description', 'city':'City', 'price':'Price', 'bath':'Bath', 'bed':'Bed', 'area':'Area', 'date':'Date', 'picture':''}

class statForm(forms.ModelForm):
    class Meta:
        model = stats
        fields = '__all__'
        labels = {'Year':'year','Month':'month', 'Sale':'sale'}