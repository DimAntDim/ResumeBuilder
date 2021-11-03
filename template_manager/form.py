from .models import Education, EmploymentHistory, Languages, Resume, Skills
from django import forms
from django.contrib.auth import get_user_model

user_model = get_user_model()

def get_resume():
    resume = Resume.objects.get(user_id=user_model)
    return resume
class PersonalInfoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['user'].widget.attrs['disabled'] = 'disabled'
        self.fields['user'].widget = forms.HiddenInput()   
        self.fields['first_name'].widget.attrs.update({'class': 'input-field', 'placeholder':'First name'})
        self.fields['photo'].widget.attrs.update({'class': 'input-field', 'value':'Upload photo'})
        self.fields['last_name'].widget.attrs.update({'class': 'input-field', 'placeholder':'Last name'})
        self.fields['address'].widget.attrs.update({'class': 'input-field', 'placeholder':'Address'})
        self.fields['city'].widget.attrs.update({'class': 'input-field', 'placeholder':'City'})
        self.fields['country'].widget.attrs.update({'class': 'input-field', 'placeholder':'Country'})
        self.fields['phone'].widget.attrs.update({'class': 'input-field', 'placeholder':'Phone number'})
        self.fields['contact_email'].widget.attrs.update({'class': 'input-field', 'placeholder':'Email'})
        self.fields['about_me'].widget.attrs.update({'class': 'input-field', 'rows': '3', 'placeholder':'Tell something about You'})
    class Meta:
        model = Resume
        fields = '__all__'


class SkillsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['resume'].widget = forms.HiddenInput()     
        self.fields['name'].widget.attrs.update({'class': 'input-field', 'placeholder':'Add skill'})
    class Meta:
        model = Skills
        fields = '__all__'


class EducationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['resume'].widget = forms.HiddenInput()    
        self.fields['school_name'].widget.attrs.update({'class': 'input-field', 'placeholder':'School name'})
        self.fields['degree'].widget.attrs.update({'class': 'input-field', 'placeholder':'Degree'})
        self.fields['start'].widget = forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'})
        self.fields['end'].widget = forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'})
    class Meta:
        model = Education
        fields = '__all__'

class EmploymentHistoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['resume'].widget = forms.HiddenInput()   
        self.fields['company_name'].widget.attrs.update({'class': 'input-field', 'placeholder':'Company name'})
        self.fields['role'].widget.attrs.update({'class': 'input-field', 'placeholder':'Role'})
        self.fields['start'].widget = forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'})
        self.fields['end'].widget = forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'})
        self.fields['description'].widget.attrs.update({'class': 'input-field', 'rows': '3', 'placeholder':'Tell about this job'})
    class Meta:
        model = EmploymentHistory 
        fields = '__all__'


class LanguagesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  
        self.fields['resume'].widget = forms.HiddenInput()  
        self.fields['language'].widget.attrs.update({'class': 'input-field', 'placeholder':'Add language'})
    class Meta:
        model = Languages 
        fields = '__all__'