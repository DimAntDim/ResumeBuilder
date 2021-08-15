
from .models import Education, Employment_history, Languages, Skills, User_Templates
from accounts.models import Profile
from django.contrib import admin

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(User_Templates)
class User_TemplatesAdmin(admin.ModelAdmin):
    pass

@admin.register(Languages)
class LanguagesAdmin(admin.ModelAdmin):
    pass

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    pass
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass

@admin.register(Employment_history)
class Employment_historyAdmin(admin.ModelAdmin):
    pass