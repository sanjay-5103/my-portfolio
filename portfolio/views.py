from django.shortcuts import render
from django.http import HttpResponse
from .models import Project,Certification
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    about_text = """
    I’m a passionate and dedicated engineering graduate who enjoys building creative solutions to real-world problems.
    I thrive in collaborative environments, love sharing ideas, and constantly seek opportunities to learn and grow.
    Challenges motivate me, and I approach them with a positive mindset and strong determination.
    """

    certifications = Certification.objects.all()
    skills = [
        "Python",
        "Django",
        "Java",
        "Machine Learning",
        "SQL",
        "HTML & CSS",
        "JavaScript"
    ]

    return render(
        request,
        'portfolio/about.html',
        {
            'about_text': about_text,
            'certifications': certifications,
            'skills': skills
        }
    )

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def contact(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                f"Message from {form.cleaned_data['name']}",
                form.cleaned_data['message'],
                form.cleaned_data['email'],
                [settings.DEFAULT_FROM_EMAIL],
            )
            success = True
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form, 'success': success})