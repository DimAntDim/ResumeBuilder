from accounts.views import complete_profile, edit_profile, user_home_page
from django.urls import path

urlpatterns = [
     path('', user_home_page, name='user home page'),
     path('complete/', complete_profile, name='complete profile'),
     path('edit-profile/<int:pk>', edit_profile, name='edit profile'),
]