from template_manager.models import Template
from django.contrib import admin

@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    pass
