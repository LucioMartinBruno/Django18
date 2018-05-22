from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from .forms import ContactForm, SignUpForm
from django.utils import timezone
from .models import Post


# Create your views here.

def Home(request):
	
	title= "Welcome"
	form = SignUpForm(request.POST or None)
	context = {
				"title":title,
	    		"form":form,

		    		}
	if form.is_valid():
		istance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"

		istance.full_name = full_name
		istance.save
		context = {
			"title":"Thank you"
			}

	return render(request,"home.html",context)

def contact(request):
	form= ContactForm(request.POST or None)
	title="Kontakt aufnehmen"
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_full_name = form.cleaned_data.get("full_name")
		form_message = form.cleaned_data.get("message")
		
		subject ="Site contact form"
		from_email= settings.EMAIL_HOST_USER
		to_email = [from_email, "youothereamail@gmail.com"]
		contact_message = "%s:%s via %s"%(form_full_name,form_message, form_email)
		some_html_message= """<h1>hello</h1>"""
		send_mail(subject,
			contact_message, 
			from_email,
			to_email, 
			html_message=some_html_message,
			fail_silently=False)


	context = {
		"form" : form,
		"title": title
	}

	return render(request,"forms.html", context)



def post_list(request):
   
    posts = Post.objects.all()
    
    return render(request, "arduino.html", {"posts": posts})

