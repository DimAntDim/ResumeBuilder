from template_manager.models import TemplateStyle
from django.contrib import admin

@admin.register(TemplateStyle)
class TemplateAdmin(admin.ModelAdmin):
    pass
