from template_manager.views import all_templates, generate_template, template_details
from django.urls import path

urlpatterns = [
     path('', all_templates, name='all templates'),
     path('details/<int:pk>', template_details, name='template details'),
     path('generate/<int:pk>', generate_template, name='generate template'),
]