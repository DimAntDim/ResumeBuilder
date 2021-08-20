from django.contrib.auth import get_user_model
from django.test import TestCase
from template_manager.models import TemplateStyle

UserModel = get_user_model()


class MainTestCase(TestCase):
    EMAIL = 'test@test.com'
    PASSWORD = 'test123test123'

    def setUp(self):
        self.user = UserModel.objects.create_user(
            email=MainTestCase.EMAIL,
            password=MainTestCase.PASSWORD,
        )
        self.user.is_active = True
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def create_new_user(self):
        self.new_user = UserModel.objects.create(
            email='new@new.com',
            password=MainTestCase.PASSWORD,
        )
        self.new_user.is_active = True
        self.new_user.save()

    def create_template(self):
        self.template = TemplateStyle.objects.get(
            id=1,
            name="Template1",
            image="img/cv_templates/template1.jpg",
            css_file="static/css/cv_templates/template1.css", 
        )
