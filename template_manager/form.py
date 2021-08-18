from .models import CustomUser, Education, Employment_history, Languages, PersonalInfo, Skills
from django import forms
from django.contrib.auth import get_user_model

user_model = get_user_model()
class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = '__all__'


class SkillsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(SkillsForm, self).__init__(*args, **kwargs)
       self.fields['user'].widget.attrs['readonly'] = True

    class Meta:
        model = Skills
        fields = '__all__'


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'


class EmploymentHistoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(EmploymentHistoryForm, self).__init__(*args, **kwargs)
       self.fields['user'].widget.attrs['readonly'] = True

    class Meta:
        model = Employment_history 
        fields = '__all__'


class LanguagesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(LanguagesForm, self).__init__(*args, **kwargs)
       self.fields['user'].widget.attrs['readonly'] = True

    class Meta:
        model = Languages 
        fields = '__all__'