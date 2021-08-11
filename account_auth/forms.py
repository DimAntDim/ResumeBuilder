from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


UserModel = get_user_model()

class LogInForm(forms.Form):
    user = None
    email= forms.CharField(
        max_length=100,
        widget= forms.EmailInput(
            attrs={
                'class':'input-field',
                'placeholder': 'User email',
                }
            )
        )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'input-field',
                'placeholder': 'Password'
            }
        ),
    )

    def clean_password(self):
        self.user = authenticate(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
        )

        if not self.user:
            raise ValidationError('Email and/or password incorrect')

    def save(self):
        return self.user


class RegisterForm(UserCreationForm):
    email= forms.CharField(
        max_length=100,
        widget= forms.EmailInput(
            attrs={
                'class':'input-field',
                'placeholder': 'user@email.com',
                }
            )
        )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'input-field',
                'placeholder': 'Enter password',
            }
        ),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'input-field',
                'placeholder': 'Re-type password',
            }
        ),
    )    

    class Meta:
        model = UserModel
        fields = ['email', 'password1', 'password2',]
        
