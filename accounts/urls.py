from .views import edit_template, template_education, template_empl_history, template_languages, template_personal_info, template_skills
from accounts.views import complete_profile, edit_profile, user_home_page
from django.urls import path

urlpatterns = [
     path('<int:pk>', user_home_page, name='user home page'),
     path('complete/', complete_profile, name='complete profile'),
     path('edit-profile/<int:pk>', edit_profile, name='edit profile'),
     path('edit/<int:pk>', edit_template, name='edit template'),
     path('edit/personal-info/', template_personal_info, name='template personal info'),
     path('edit/skills/', template_skills, name='template skills'),
     path('edit/education/', template_education, name='template education'),
     path('edit/employment-history/', template_empl_history, name='template empl history'),
     path('edit/languages/', template_languages, name='template languages'),
]