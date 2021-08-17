
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
    def has_module_permission(self, request):
        return False

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

@admin.register(Employment_history)
class Employment_historyAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False