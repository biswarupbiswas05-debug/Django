from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
 
def home(request):
    return render(request, 'website/index.html')
def about(request):
    return HttpResponse("about")
def contact(request):
    return HttpResponse("contact")
def services(request):
    return HttpResponse("services")


