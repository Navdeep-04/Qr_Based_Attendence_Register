from django.shortcuts import render
from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings

def index(request,):
    send_mail(
        'Attendance form',
        message,
        'settings.EMAIL_HOST_USER',
        ['sri422001@gamil.com'],
        fail_silently=False)
    
    return render(request,'index.html')