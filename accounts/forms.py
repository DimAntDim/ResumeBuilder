from .models import Profile
from django import forms
from django.contrib.auth import get_user_model


UserModel = get_user_model()

class ProfileForm(forms.ModelForm): 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'input-field', 'placeholder':'First name'})
        self.fields['profile_image'].widget.attrs.update({'class': 'input-field', 'value':'Upload photo'})
        self.fields['last_name'].widget.attrs.update({'class': 'input-field', 'placeholder':'Last name'})
    class Meta:
        model = Profile 
        fields = "__all__"
        exclude = ('user', 'is_complete', 'template_selected',)




