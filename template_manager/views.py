from django.db.models.query import InstanceCheckMeta
from accounts.models import Profile
from .form import EducationForm, EmploymentHistoryForm, LanguagesForm, PersonalInfoForm, SkillsForm
from django.shortcuts import redirect, render
from .models import CustomUser, Skills, TemplateStyle
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
    if request.method == 'POST':
        pass

    context = {
        "template": template,
    }
    return render(request, 'templates/template_details.html', context)

def generate_template(requset, pk):
    style = TemplateStyle.objects.get(pk=pk)
    style_path = os.path.join(STATICFILES_DIRS, str(style.css_file))

    context = {
        "style_path": style_path,
    }
    return render(requset, "shared/resume_base.html", context)

def edit_template(request, pk):
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
        else:
            return render(request, 'resume/personal_info.html', {'errors':form.errors})

    form = PersonalInfoForm()
    form.user = request.user
    context = {
        "form": form,
    }
    return render(request, 'resume/personal_info.html', context)

def template_skills(request):
    user = request.user
    skills = Skills.objects.all().filter(user_id=user.id)
    if request.method == 'POST':
        form = SkillsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('template skills')
        else:
            return render(request, 'resume/skills.html', {'errors':form.errors})

    form = SkillsForm()
    form.user = request.user
    context = {
        "form": form,
        "skills": skills,
    }
    return render(request, 'resume/skills.html', context)

def template_education(request):
    if request.method == 'POST':
        form = LanguagesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('template empl history')
        else:
            return render(request, 'resume/languages.html', {'errors':form.errors})
    
    form = EducationForm()
    form.user = request.user
    context = {
        "form": form,
    }
    return render(request, 'resume/education.html', context)

def template_empl_history(request):
    if request.method == 'POST':
        form = EmploymentHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('template languages')
        else:
            return render(request, 'resume/employment_history.html', {'errors':form.errors})

    form = EmploymentHistoryForm()
    form.user = request.user
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
