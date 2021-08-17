from django.shortcuts import render
from .models import TemplateStyle
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
