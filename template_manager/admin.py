from template_manager.models import TemplateStyle
from django.contrib import admin

@admin.register(TemplateStyle)
class TemplateAdmin(admin.ModelAdmin):
    pass

# @admin.register(Languages)
# class LanguagesAdmin(admin.ModelAdmin):
#     def has_module_permission(self, request):
#         return False

# @admin.register(Skills)
# class SkillsAdmin(admin.ModelAdmin):
#     def has_module_permission(self, request):
#         return False
# @admin.register(Education)
# class EducationAdmin(admin.ModelAdmin):
#     def has_module_permission(self, request):
#         return False

# @admin.register(Employment_history)
# class Employment_historyAdmin(admin.ModelAdmin):
#     def has_module_permission(self, request):
#         return False