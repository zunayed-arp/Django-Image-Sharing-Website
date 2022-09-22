from django import forms

from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserCreationForm
from .models import Profile

User = get_user_model()



class UserCreationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email','password','password2']
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email']
        
class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields =['bio','image']
    
