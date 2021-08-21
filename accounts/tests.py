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


   