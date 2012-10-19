# Create your views here.
from django.shortcuts import render_to_response

def home(request):
	return render_to_response("index.html")

def contact(request):
	return render_to_response("contact.html")

def about(request):
	return render_to_response("about.html")

def services(request):
	return render_to_response("services.html")
