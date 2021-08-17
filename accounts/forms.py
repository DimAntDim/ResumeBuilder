from .models import Profile
from django import forms
from django.contrib.auth import get_user_model


UserModel = get_user_model()

class ProfileForm(forms.ModelForm):    
    class Meta:
        model = Profile 
        fields = "__all__"
        exclude = ('user', 'is_complete')




