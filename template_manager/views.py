from django.shortcuts import render
from .models import Template
import os
from django.contrib.auth.decorators import login_required

def all_templates(request):
    templates = Template.objects.all()
    context= {
        "templates": templates, 
    }
    return render(request, "templates_page.html", context)

def template_details(request, pk):
    template = Template.objects.get(pk=pk)
    if request.method == 'POST':
        pass

    context = {
        "template": template,
    }
    return render(request, 'templates/template_details.html', context)


def generate_template(requset, pk):
    template = Template.objects.get(pk=pk)
    template_html = os.path.join("CV_Templates", str(template.file))

    context = {
        "template": template,
    }
    return render(requset, template_html, context)
