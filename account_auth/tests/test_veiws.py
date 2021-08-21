from account_auth.forms import RegisterForm
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class RegisterViewTest(TestCase):
    def test_register_render_template(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='account/register.html')
        self.assertIsInstance(response.context['form'], RegisterForm)

    def test_register_create_user(self):
        response = self.client.post(reverse('register'),
                                    data={
                                        'email': "test@test.com",
                                        'password': "test",
                                        'password2': "test",
                                    },
                                    follow=True)
        self.assertEqual(response.status_code, 200)

class LoginViewTest(TestCase):
    def test_login_success_redirect_user_home_page(self):
        response = self.client.post(reverse('login'), data={'email': 'test@test.test', 'password': 'test'})
        self.assertEqual(200, response.status_code)



class LogOutViewTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            email='test@textcom',
            password = 'test',
            )
    def tearDown(self):
        self.user.delete()

    def test_logout_success_redirect_index(self):
        self.client.login(email="test@test.com", password='text')
        response = self.client.get(reverse('logout'))
        self.assertEqual(302, response.status_code)

