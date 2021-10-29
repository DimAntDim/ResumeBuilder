from .views import all_templates, delete_resume, save_resume, template_details,\
template_education, template_empl_history, template_languages, template_personal_info, template_preview, template_remove_education, template_remove_empl_history, template_remove_language, template_remove_skill, template_render, template_skills
from django.urls import path

urlpatterns = [
     path('', all_templates, name='all templates'),
     path('details/<int:pk>', template_details, name='template details'),
     path('edit/personal-info/<int:pk>', template_personal_info, name='template personal info'),
     path('edit/skills/', template_skills, name='template skills'),
     path('edit/skills/remove/<int:pk>', template_remove_skill, name='template remove skill'),
     path('edit/education/', template_education, name='template education'),
     path('edit/education/remove/<int:pk>', template_remove_education, name='template remove education'),
     path('edit/employment-history/', template_empl_history, name='template empl history'),
     path('edit/employment-history/remove/<int:pk>', template_remove_empl_history, name='template remove empl history'),
     path('edit/languages/', template_languages, name='template languages'),
     path('edit/languages/remove/<int:pk>', template_remove_language, name='template remove language'),
     path('render/preview', template_preview, name='template preview'),
     path('render/generate', template_render, name='template render'),
     path('save/', save_resume, name='save resume'),
     path('delete/', delete_resume, name='delete resume'),
]