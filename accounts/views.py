from django.contrib.auth import get_user_model
from template_manager.models import TemplateStyle
from .forms import EducationForm, EmploymentHistoryForm, LanguagesForm, PersonalInfoForm, SkillsForm
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from accounts.forms import ProfileForm
from django.shortcuts import redirect, render

User = get_user_model()

@login_required
def user_home_page(request, pk):
    profile = Profile.objects.get(pk=pk)
    if profile.is_complete:
        context = {
            "profile": profile,
        }
        return render(request, 'profile/user_home_page.html', context)
    else:
        return redirect('complete profile')



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

def edit_template(request, pk):
    style = TemplateStyle.objects.get(pk=pk)
    context = {
        "style": style,
    }
    return render(request, 'resume/base_edit.html', context)


def template_personal_info(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('template skills')
        else:
            return render(request, 'resume/personal_info.html', {'errors':form.errors})

    form = PersonalInfoForm()
    context = {
        "form": form,
    }
    return render(request, 'resume/personal_info.html', context)

def template_skills(request):
    if request.method == 'POST':
        form = SkillsForm(request.POST, instance=request.user.id)
        if form.is_valid():
            form.save()
            return redirect('template education')
        else:
            return render(request, 'resume/skills.html', {'errors':form.errors})

    form = SkillsForm()
    context = {
        "form": form,
    }
    return render(request, 'resume/skills.html', context)

def template_education(request):
    if request.method == 'POST':
        form = LanguagesForm(request.POST, instance=request.user.id)
        if form.is_valid():
            form.save()
            return redirect('template empl history')
        else:
            return render(request, 'resume/languages.html', {'errors':form.errors})
    
    form = EducationForm()
    context = {
        "form": form,
    }
    return render(request, 'resume/education.html', context)


def template_empl_history(request):
    if request.method == 'POST':
        form = EmploymentHistoryForm(request.POST, instance=request.user.id)
        if form.is_valid():
            form.save()
            return redirect('template languages')
        else:
            return render(request, 'resume/employment_history.html', {'errors':form.errors})

    form = EmploymentHistoryForm()
    context = {
        "form": form,
    }
    return render(request, 'resume/employment_history.html', context)



def template_languages(request):
    if request.method == 'POST':
        form = LanguagesForm(request.POST, instance=request.user.id)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'resume/languages.html', {'errors':form.errors})
    form = LanguagesForm()
    context = {
        "form": form,
    }
    return render(request, 'resume/languages.html', context)

