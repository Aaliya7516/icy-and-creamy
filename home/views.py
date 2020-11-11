from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime
# Create your views here.
def index(request):
    context = {
        "var1": "Strawberry",
        "var2": "Choco chips"
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        topic = request.POST.get('topic')
        contact = Contact(name = name, email=email, phone=phone, topic=topic, date=datetime.today())
        contact.save()
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("this is used for textual output.")