from django.contrib.auth import get_user_model
from accounts.forms import ProfileForm
from account_auth.models import CustomUser
from django.test.client import Client
from django.urls import reverse
from django.test import TestCase


class TestAllProfileView(TestCase):
    def setUp(self):
        self.client = Client()

    def  test_complete_profile_page_url(self):
        self.user = CustomUser.objects.create(email='test@test.com', password='test1234test')
        self.client.force_login(self.user)
        response = self.client.get(reverse('complete profile'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'profile/complete_profile.html')


    def test_complete_form_safe_when_valid(self):
        data = {
            "first_name": "Dimitar",
            "last_name": "Dimitrov",
            "profile_image": "/media/profile/img/img.jpg",
        }
        form = ProfileForm(data)
        self.assertTrue(form.is_valid)


    