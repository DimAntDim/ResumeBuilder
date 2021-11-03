from django.http import request
from accounts.models import Profile
from .form import EducationForm, EmploymentHistoryForm, LanguagesForm, PersonalInfoForm, SkillsForm
from django.shortcuts import redirect, render
from .models import Education, EmploymentHistory, Languages, Resume, Skills, TemplateStyle
from config.settings import STATICFILES_DIRS
import os
from django.contrib.auth.decorators import login_required
from django.core import serializers


def get_resume(request):
    resume = Resume.objects.filter(user=request.user.pk).order_by('-pk')[0]
    return resume

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

def template_personal_info(request, pk):
    profile = Profile.objects.get(pk=request.user.pk)
    profile.template_selected = pk
    profile.save()
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('template skills')
        else:
            return redirect('template personal info', pk)
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

    skills = Skills.objects.all().filter(resume=get_resume(request))
    form = SkillsForm(initial={'resume':get_resume(request)})
    context = {
        "form": form,
        "skills": skills,
    }
    return render(request, 'resume/skills.html', context)

def template_remove_skill(request, pk):
    skill = Skills.objects.get(pk=pk)
    skill.delete()
    return redirect('template skills')

def template_education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('template education')

    educations = Education.objects.all().filter(resume=get_resume(request))
    form = EducationForm(initial={'resume':get_resume(request)})
    context = {
        "form": form,
        "educations": educations,
    }
    return render(request, 'resume/education.html', context)

def template_remove_education(request, pk):
    education = Education.objects.get(pk=pk)
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

    empl_history = EmploymentHistory.objects.all().filter(resume=get_resume(request))
    form = EmploymentHistoryForm(initial={'resume':get_resume(request)})
    context = {
        "form": form,
        "empl_history": empl_history,
    }
    return render(request, 'resume/employment_history.html', context)

def template_remove_empl_history(request, pk):
    empl = EmploymentHistory.objects.get(pk=pk)
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

    languages = Languages.objects.all().filter(resume=get_resume(request))
    form = LanguagesForm(initial={'resume':get_resume(request)})
    context = {
        "form": form,
        "languages": languages,
    }
    return render(request, 'resume/languages.html', context)


def template_remove_language(request, pk):
    language = Languages.objects.get(pk=pk)
    language.delete()
    return redirect('template languages')


def template_preview(request):
    profile = Profile.objects.get(pk=request.user.pk) 
    template = TemplateStyle.objects.get(pk=profile.template_selected)
    resume = get_resume(request)
    personal_info = Resume.objects.filter(user_id=request.user.pk).order_by('-pk')[0]
    photo = personal_info.photo.url
    skills = Skills.objects.all().filter(resume_id=resume.pk)
    education = Education.objects.all().filter(resume_id=resume.pk)
    empl_history = EmploymentHistory.objects.all().filter(resume_id=resume.pk)
    languages = Languages.objects.all().filter(resume_id=resume.pk)
    context = {
        "template": template,
        "personal_info": personal_info.__dict__,
        "skills": skills,
        "education": education,
        "empl_history": empl_history,
        "languages": languages,
        "photo": photo,
    }
    return render(request, "shared/resume_preview.html", context)

def template_render(request):
    profile = Profile.objects.get(pk=request.user.pk)
    resume = get_resume(request)
    template = TemplateStyle.objects.get(pk=profile.template_selected)
    style_path = f'/static/css/cv_templates/{template.css_file.name}'
    personal_info = Resume.objects.filter(user_id=request.user.pk).order_by('-pk')[0]
    photo = personal_info.photo.url
    skills = Skills.objects.all().filter(resume_id=resume.pk)
    education = Education.objects.all().filter(resume_id=resume.pk)
    empl_history = EmploymentHistory.objects.all().filter(resume_id=resume.pk)
    languages = Languages.objects.all().filter(resume_id=resume.pk)
    context = {
        "personal_info": personal_info.__dict__,
        "skills": skills,
        "style_path": style_path,
        "education": education,
        "empl_history": empl_history,
        "languages": languages,
        "photo": photo,
    }
    return render(request, "shared/resume_base.html", context)
