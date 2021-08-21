from django.test import TestCase
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class SignalCreateUserTest(TestCase):
    def test_superuserCreated_isActive(self):
        superuser = UserModel.objects.create_superuser(email='test@test.test', password='test1234test')
        self.assertTrue(superuser.is_active)