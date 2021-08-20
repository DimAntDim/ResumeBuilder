from accounts.models import Profile
from account_auth.models import CustomUser
from django.test import TestCase

class TestCustomUserModel(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            email = "test@test.com",
            is_staff = False,            
        )
    
    def test_custom_user_pass(self):
        data = self.user
        self.assertTrue(isinstance(data, CustomUser))

    
