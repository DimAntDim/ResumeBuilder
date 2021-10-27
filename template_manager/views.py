from accounts.models import Profile
from .form import EducationForm, EmploymentHistoryForm, LanguagesForm, PersonalInfoForm, SkillsForm
from django.shortcuts import redirect, render
from .models import Resume, TemplateStyle
from config.settings import STATICFILES_DIRS
import os
from django.contrib.auth.decorators import login_required


def all_templates(request):
    templates = TemplateStyle.objects.all()
    context= {
        "templates": templates, 
    }
    return render(request, "templates_page.html", context)

def template_details(request, pk):
    template = TemplateStyle.objects.get(pk=pk)
    context = {
        "template": template,
    }
    return render(request, 'templates/template_details.html', context)

def select_template(request, pk):
    profile = Profile.objects.get(pk=request.user.pk)
    profile.template_selected = pk
    profile.save()
    style = TemplateStyle.objects.get(pk=pk)
    context = {
        "style": style,
    }
    return render(request, 'resume/base_edit.html', context)


def template_personal_info(request):
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('template skills')
    form = PersonalInfoForm(initial={'user':request.user})
    context = {
        "form": form,
    }
    return render(request, 'resume/personal_info.html', context)

def template_skills(request):
    if request.method == 'POST':
        form = SkillsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('template skills')

    skills = Resume.skills.objects.all().filter(user=request.user)
    form = SkillsForm(initial={'user':request.user})
    context = {
        "form": form,
        "skills": skills,
    }
    return render(request, 'resume/skills.html', context)

def template_remove_skill(request, pk):
    skill = Resume.skills.objects.get(pk=pk)
    skill.delete()
    return redirect('template skills')

def template_education(request):
    if request.method == 'POST':
        form = Resume(request.POST)
        if form.is_valid():
            form.save()
            return redirect('template education')

    educations = Resume.education.objects.all().filter(user=request.user)
    form = EducationForm(initial={'user':request.user})
    context = {
        "form": form,
        "educations": educations,
    }
    return render(request, 'resume/education.html', context)

def template_remove_education(request, pk):
    education = Resume.education.objects.get(pk=pk)
    education.delete()
    return redirect('template education')


def template_empl_history(request):
    if request.method == 'POST':
        form = EmploymentHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('template empl history')
        else:
            return render(request, 'resume/employment_history.html')

    empl_history = Resume.employment_history.objects.all().filter(user=request.user)
    form = EmploymentHistoryForm(initial={'user':request.user})
    context = {
        "form": form,
        "empl_history": empl_history,
    }
    return render(request, 'resume/employment_history.html', context)

def template_remove_empl_history(request, pk):
    empl = Resume.employment_history.objects.get(pk=pk)
    empl.delete()
    return redirect('template empl history')

def template_languages(request):
    if request.method == 'POST':
        form = LanguagesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('template languages')
        else:
            print(form.errors)
            return render(request, 'resume/languages.html')

    languages = Resume.languages.objects.all().filter(user=request.user)
    form = LanguagesForm(initial={'user':request.user})
    context = {
        "form": form,
        "languages": languages,
    }
    return render(request, 'resume/languages.html', context)


def template_remove_language(request, pk):
    language = Resume.languages.objects.get(pk=pk)
    language.delete()
    return redirect('template languages')


def template_preview(request):
    profile = Profile.objects.get(pk=request.user.pk) 
    template = TemplateStyle.objects.get(pk=profile.template_selected)
    personal_info = Resume.personal_infoersonalInfo.objects.all().filter(user=request.user)
    skills = Resume.skills.objects.all().filter(user=request.user)
    education = Resume.education.objects.all().filter(user=request.user)
    empl_history = Resume.employment_history.objects.all().filter(user=request.user)
    languages = Resume.languages.objects.all().filter(user=request.user)
    context = {
        "template": template,
        "personal_info": personal_info,
        "skills": skills,
        "education": education,
        "empl_history": empl_history,
        "languages": languages,
    }
    return render(request, "shared/resume_preview.html", context)

def template_render(request):
    profile = Profile.objects.get(pk=request.user.pk) 
    template = TemplateStyle.objects.get(pk=profile.template_selected)
    style_path = f'/static/css/cv_templates/{template.css_file.name}'
    personal_info = Resume.personal_info.objects.all().filter(user=request.user)
    skills = Resume.skills.objects.all().filter(user=request.user)
    education = Resume.education.objects.all().filter(user=request.user)
    empl_history = Resume.employment_history.objects.all().filter(user=request.user)
    languages = Resume.languages.objects.all().filter(user=request.user)
    context = {
        "style_path": style_path,
        "personal_info": personal_info,
        "skills": skills,
        "education": education,
        "empl_history": empl_history,
        "languages": languages,
    }
    return render(request, "shared/resume_base.html", context)