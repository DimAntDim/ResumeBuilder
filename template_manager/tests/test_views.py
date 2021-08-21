from account_auth.models import CustomUser
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
