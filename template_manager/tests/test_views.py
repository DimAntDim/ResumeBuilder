from template_manager.models import Education, EmploymentHistory, PersonalInfo
from django.test.client import Client
from template_manager.form import PersonalInfoForm
from django.contrib.auth import get_user_model
from account_auth.models import CustomUser
from django.urls import reverse
from django.test import TestCase


class TestAllTemplatesView(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_all_templates_url(self):
        response = self.client.get(reverse('all templates'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'templates_page.html')
    
    def test_personal_information_url(self):
        self.user = CustomUser.objects.create(email='test@test.com', password='test1234test')
        self.client.force_login(self.user)
        response = self.client.get(reverse('template personal info'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'resume/personal_info.html')

    def test_skills_url(self):
        self.user = CustomUser.objects.create(email='test@test.com', password='test1234test')
        self.client.force_login(self.user)
        response = self.client.get(reverse('template skills'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'resume/skills.html')

    def test_education_url(self):
        self.user = CustomUser.objects.create(email='test@test.com', password='test1234test')
        self.client.force_login(self.user)
        response = self.client.get(reverse('template education'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'resume/education.html')

    def test_emp_history_url(self):
        self.user = CustomUser.objects.create(email='test@test.com', password='test1234test')
        self.client.force_login(self.user)
        response = self.client.get(reverse('template empl history'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'resume/employment_history.html')

    def test_languages_url(self):
        self.user = CustomUser.objects.create(email='test@test.com', password='test1234test')
        self.client.force_login(self.user)
        response = self.client.get(reverse('template education'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'resume/education.html')

    def test_personal_info_form_safe_when_valid(self):
        data = {
            "user": get_user_model(),
            "first_name": "Dimitar",
            "last_name": "Dimitrov",
            "address": "Trakia",
            "city": "Plovdiv",
            "country": "BG",
            "phone": "1234",
            "contact_email": "d@d.com",
            "abount_me": "me",
        }
        form = PersonalInfoForm(data)
        self.assertTrue(form.is_valid)

    def test_template_skills_form_safe_when_valid(self):
        data = {
            "user": get_user_model(),
            "name": "Templare",
        }
        form = PersonalInfoForm(data)
        self.assertTrue(form.is_valid)

    def test_educations_form_safe_when_valid(self):
        data = {
            "user": get_user_model(),
            "school_name": "School",
            "degree": "Bachelor",
            "start": "12/2/2001",
            "end": "12/2/2001",
        }
        form = PersonalInfoForm(data)
        self.assertTrue(form.is_valid)

    def test_EmploymentHistory_form_safe_when_valid(self):
        data = {
            "user": get_user_model(),
            "company_name": "Company",
            "role": "Role",
            "start": "12/2/2001",
            "end": "12/2/2001",
            "description": "Job",
        }
        form = PersonalInfoForm(data)
        self.assertTrue(form.is_valid)

    def test_lenguages_form_safe_when_valid(self):
        data = {
            "user": get_user_model(),
            "language": "Spanish",
        }
        form = PersonalInfoForm(data)
        self.assertTrue(form.is_valid)


class TestTemplateManagerAllPosts(TestCase):
    def setUp(self):
        self.test_client = Client()
        self.lang = "Eng"
        self.empl = EmploymentHistory(
             user= get_user_model(),
            company_name="Company",
            role="Role",
            start= "12/2/2001",
            end= "12/2/2001",
            description= "Job",
        )
        self.education = Education(
            user= get_user_model(),
            school_name= "School",
            degree= "Bachelor",
            start="12/2/2001",
            end= "12/2/2001",
        )

        self.skill = "Django",
        self.personal_info = PersonalInfo(
            user= get_user_model(),
            first_name= "Dimitar",
            last_name= "Dimitrov",
            address= "Trakia",
            city= "Plovdiv",
            country= "BG",
            phone= "1234",
            contact_email= "d@d.com",
            abount_me= "me",
        )
