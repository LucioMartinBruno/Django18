from django.shortcuts import render
# Create your views here.

def About(request):
	title= "About me"
	context={
		"title": title,
		}
	return render(request,"about.html", context)


def arduino(request):
	title= "About me"
	context={
		"title": title,
		}
	return render(request,"arduino.html", context)


def raspberry(request):
	title= "About me"
	context={
		"title": title,
		}
	return render(request,"raspberry.html", context)

