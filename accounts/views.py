from template_manager.models import Education, EmploymentHistory, Languages, PersonalInfo, Skills
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from accounts.forms import ProfileForm
from django.shortcuts import redirect, render

User = get_user_model()

@login_required
def user_home_page(request):
    profile = Profile.objects.get(pk=request.user.pk)
    personal_info = PersonalInfo.objects.all().filter(user=request.user)
    skills = Skills.objects.all().filter(user=request.user)
    education = Education.objects.all().filter(user=request.user)
    empl_history = EmploymentHistory.objects.all().filter(user=request.user)
    languages = Languages.objects.all().filter(user=request.user)
    if profile.is_complete:
        context = {
            "profile": profile,
            "personal_info": personal_info,
            "skills": skills,
            "education": education,
            "empl_history": empl_history,
            "languages": languages,
        }
        return render(request, 'profile/user_home_page.html', context)
    else:
        return redirect('complete profile')


@login_required
def complete_profile(request):
    profile = Profile.objects.get(pk=request.user.pk)
       
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile.is_complete = True
            profile.save()
            form.save()
            return redirect('user home page', pk=request.user.pk)
        else:
            form = ProfileForm(instance=profile)
            context = {
                "form": form,
            }
            return redirect('user home page', pk=request.user.pk)
        
    form = ProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'profile/complete_profile.html', context)


@login_required
def edit_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user home page', pk=pk)
        else:
            return redirect('edit profile', pk=pk)
    form = ProfileForm(instance=profile)
    context ={
        "form":form,
    }
    return render(request, 'profile/edit_profile.html', context)
