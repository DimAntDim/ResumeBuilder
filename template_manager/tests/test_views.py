from template_manager.views import all_templates
from django.http import request
from account_auth.models import CustomUser
from django.contrib.auth import get_user_model
from django.test.client import Client
from template_manager.models import PersonalInfo, TemplateStyle
from django.urls import reverse
from django.test import TestCase


class TestAllTemplatesView(TestCase):
   

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


class TestAllTemplatesGET(TestCase):
    def test_all_templates_render(self):
        request = self.factory.get('all templates')
        response = all_templates(request)
    
#class AllTemplatesPost(TestCase):
    def setUp(self):
        self.user = get_user_model()
        self.client = Client()
        self.template1 = TemplateStyle.objects.create(
            id=1,
            name="Template1",
            image="img/cv_templates/template1.jpg",
            css_file="static/css/cv_templates/template1.css", 
        )
        self.template2 = TemplateStyle.objects.create(
            id=2,
            name="Template2",
            image="img/cv_templates/template2.jpg",
            css_file="static/css/cv_templates/template2.css", 
        )
    
    # def test_personal_information_post(self):
    #     self.user = CustomUser.objects.create(email='test@test.com', password='test1234test')
    #     self.client.force_login(self.user)       
    #     self.client.post(
    #         reverse('template personal info'),
    #         PersonalInfo={
    #             'user': get_user_model,
    #             'photo': '/media/account/photo1.jpg',
    #             'first_name': 'Dimitar',
    #             'last_name': 'Dimitrov',
    #             'address': "Tarkia",
    #             'country': "BG",
    #             'phone': 1234,
    #             'contact_email': 'test@test.com',
    #             'about_me': 'This is me',
    #         }
    #     )
    #     user_personal = self.user.personalinfo_set.count()
    #     self.assertNotEqual(0, user_personal)
    