from django.test.client import Client
from template_manager.models import Education, EmploymentHistory, Languages, PersonalInfo, Skills
from account_auth.models import CustomUser
from django.test import TestCase

class TestPersonalInfoModel(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create(
            email = "dimitar@gmail.com",
            is_staff = False,            
        )
        self.data1 = PersonalInfo.objects.create(
            user = self.user,
            first_name = "Dimitar",
            last_name = "Dimitrov",
            photo = "media\profiles\photo\20210528_162445.jpg",
            address = "Trakia 19",
            city = "Popovo",
            country = "BG",
            phone = "1234",
            contact_email = "dim@gmail.com",
            about_me = "This is me", 
        )
    
    def test_personal_info_entry_pass(self):
        data = self.data1
        self.assertTrue(isinstance(data, PersonalInfo))


class TestSkillsModel(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            email = "dimitar@gmail.com",
            is_staff = False,            
        )
        self.data1 = Skills.objects.create(
            user = self.user,
            name = "Django",
        )

    def test_skills_entry_pass(self):
        data = self.data1
        self.assertTrue(isinstance(data, Skills))

    def test_personal_info_srt_return(self):
        data = self.data1
        self.assertEqual(str(data), "Django")

class TestEducationModel(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            email = "dimitar@gmail.com",
            is_staff = False,            
        )
        self.data1 = Education.objects.create(
            user = self.user,
            school_name = "Hr. Botev",
            degree = "High School",
            start = "2021-08-02",
            end="2021-08-05",
        )
    def test_education_entry_pass(self):
        data = self.data1
        self.assertTrue(isinstance(data, Education))

class TestEmploymentHistoryModel(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            email = "dimitar@gmail.com",
            is_staff = False,            
        )
        self.data1 = EmploymentHistory.objects.create(
            user = self.user,
            company_name = "IBM",
            role = "Window Cleaner",
            start = "2021-08-02",
            end="2021-08-05",
            description="The most dificult job im the world!"
        )
    def test_empl_history_entry_pass(self):
        data = self.data1
        self.assertTrue(isinstance(data, EmploymentHistory))

class TestLanguageModel(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            email = "dimitar@gmail.com",
            is_staff = False,            
        )
        self.data1 = Languages.objects.create(
            user = self.user,
            language = "English",
        )

    def test_skills_entry_pass(self):
        data = self.data1
        self.assertTrue(isinstance(data, Languages))

    def test_personal_info_srt_return(self):
        data = self.data1
        self.assertEqual(str(data), "English")
