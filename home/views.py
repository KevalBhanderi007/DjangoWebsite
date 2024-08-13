from django.shortcuts import render , HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable1" :"this is  firstvariables",
        "variable2" : "this is  secondvariables",
        "variable3" :"this is thirdvariables"
    }
    # messages.add_message(request, messages.SUCCESS, "Your message was submitted successfully.") 
    #messages.success(request, "Your message was submitted successfully.")

    # return HttpResponse("This is Homepage")
    return render(request, 'index.html',context)
def about(request):
    # return HttpResponse("This is aboutpage")
    return render(request, 'about.html')
def services(request):
    # return HttpResponse("This is servipage")
    return render(request, 'services.html')
def contact(request):
    # return HttpResponse("This is contactpage")

    if request.method == "POST" :
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        contact = Contact(name=name ,email=email ,phone=phone ,address=address ,date =datetime.today())
        contact.save()
        messages.success(request, "Your message submit successfully!")

    return render(request, 'contact.html')