from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
# Create your views here.

def accept(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone_number = request.POST.get('phone_number', '')
        summary = request.POST.get('summary', '')
        degree = request.POST.get('degree', '')
        university = request.POST.get('university', '')
        previous_work = request.POST.get('previous_work', '')
        skills = request.POST.get('skills', '')
        profile = Profile(
            name=name,
            email=email,
            phone_number=phone_number,
            summary=summary,
            degree=degree,
            university=university,
            previous_work=previous_work,
            skills=skills,
            )
        profile.save()
        
    
    return render(request, 'pdf/accept.html')


def resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')        
    
    context = {
        'user_profile': user_profile
    }
    
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
    }
    
    html = template.render(context)
    pdf = pdfkit.from_string(html, False, options)
    
    respone = HttpResponse(pdf, content_type='application/pdf')
    respone['Content-Disposition'] = 'attachment'
    filename = "resume.pdf"
    return respone


def list(request):
    profiles = Profile.objects.all()
    return render(request,'pdf/list.html',{'profiles':profiles})
