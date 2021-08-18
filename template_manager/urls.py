from .views import all_templates, generate_template, template_details, edit_template, template_edit_personal_info, \
template_education, template_empl_history, template_languages, template_personal_info, template_remove_education, template_remove_skill, template_skills
from django.urls import path

urlpatterns = [
     path('', all_templates, name='all templates'),
     path('details/<int:pk>', template_details, name='template details'),
     path('generate/<int:pk>', generate_template, name='generate template'),
     path('edit/personal-info/', template_personal_info, name='template personal info'),
     path('edit/personal-info/edit/<int:pk>', template_edit_personal_info, name='template edit personal info'),
     path('edit/skills/', template_skills, name='template skills'),
     path('edit/skills/remove/<int:pk>', template_remove_skill, name='template remove skill'),
     path('edit/education/', template_education, name='template education'),
     path('edit/education/remove/<int:pk>', template_remove_education, name='template remove education'),
     path('edit/employment-history/', template_empl_history, name='template empl history'),
     path('edit/languages/', template_languages, name='template languages'),
     path('edit/<int:pk>', edit_template, name='edit template'),
]