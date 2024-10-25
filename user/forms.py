
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailField, ModelForm

from user.models import Profile


class UserRegister(UserCreationForm):
    class Meta():
        model= User
        fields= ['username', 'email', 'password1', 'password2']
        
    def save(self, commit=True):
        user = super().save()   
        print(f'user with username {self.cleaned_data["username"]} created!')
        
        if commit:
            user.save() # Calling it later so that I can log it out first
        return user





class UpdateUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username', 'email']
    


class ProfileUpdate(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image']

