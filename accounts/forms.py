from .models import Education, PersonalInfo, Profile, Skills, User_Templates
from django import forms
from django.contrib.auth import get_user_model


UserModel = get_user_model()

class ProfileForm(forms.ModelForm):    
    class Meta:
        model = Profile 
        fields = "__all__"
        exclude = ('user', 'is_complete')


class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo 
        fields = "__all__" 

class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills 
        fields = "__all__"
class EmploymentHistoryForm(forms.ModelForm):
    class Meta:
        model = User_Templates 
        fields = ("employment_history",)

class EducationForm(forms.ModelForm):
    class Meta:
        model = User_Templates 
        fields = ("education",)



class LanguagesForm(forms.ModelForm):
    class Meta:
        model = User_Templates 
        fields = ("languages",)

