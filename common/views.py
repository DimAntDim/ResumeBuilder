from accounts.models import Profile
from django.shortcuts import render



def index(request):
    return render(request, 'home_page.html')