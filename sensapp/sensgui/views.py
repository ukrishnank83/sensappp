from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def login(request):
	send_mail('Subject here', 'Here is the message.', settings.EMAIL_HOST_USER , ['unni@qburst.com'], fail_silently=False)
	return render_to_response('login/login.html')