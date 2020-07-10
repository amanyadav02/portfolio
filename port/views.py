from django.shortcuts import render,HttpResponse
from port.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'port/home.html')
def contact(request):
    if(request.method=="POST"):
        name=request.POST.get('name')
        email=request.POST.get('email')
        area=request.POST.get('area')
        contact=Contact(name=name,email=email,area=area)
        contact.save()
        messages.success(request,'Your Message Has Been Sent')
    return render(request,'port/contact.html')

