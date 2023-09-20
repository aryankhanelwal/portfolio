from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.views import generic
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail




def firstpage(request ):
    return render(request, 'firstpage.html')

def contact_me(request):
    if request.method == "POST":
        form = insertdata(request.POST) 
        if form.is_valid():#The is_valid() method is used to perform validation for each field of the form, it is defined in Django Form class. It returns True if data is valid and place all data into a cleaned_data attribute.
            name = form.cleaned_data['name'] #cleaned_data is a dictionary of form fields and their values.
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            project_Summary = form.cleaned_data['project_Summary']
       
        subject = f"{subject}"
        project_Summary = f"{project_Summary}"
        from_email = '{email}'
        recipient_list = ['2002ak2002@gmail.com']
        message_body = f"Name: {name}\nEmail: {email}\nMessage: {project_Summary}"
            
        send_mail(subject, message_body, from_email, recipient_list)#send_mail() function is used to send a mail to the recipient.
        return render(request, 'form.html', {'form': form})
    else:
        form = insertdata()
    return render(request, 'form.html', {'form': form})
    
def mywork(request ):
    return render(request, 'mywork.html')
def mywork1(request ):
    return render(request, 'mywork1.html')
def blog(request ):
    return render(request, 'base.html')


def aboutus(request ):
    return render(request, 'aboutus.html')

def index(request ):
    return render(request, 'index.html')
def postdetai(request ):
    return render(request, 'post_details.html')
def post_Detail(request, slug):
    post= Post.objects.filter(slug=slug).first()
    return render(request, 'post_details.html',{'post':post})

def frontpage(request):
	posts = Post.objects.all()

	return render(request, 'index.html', {'posts': posts})
    
