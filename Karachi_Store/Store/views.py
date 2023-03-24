from django.shortcuts import render

from django.http import HttpResponse

from .models import Product 
from Store.models import Contact 

# Create your views here.

def index(request): #new

    # products =  Product.get_all_Products()
    products = Product.objects.all()
    
    return render(request, "index.html",{'products': products})

def Special_Offer(request):
    return render(request, "special_offer.html")

def Delivery(request):
    return render(request, "normal.html")

def contact(request):
    return render(request, "contact.html",{})

def Message(request):
    if request.method == "POST":
        n = request.POST["c_name"]
        e = request.POST["c_email"]
        s = request.POST["c_subject"]
        m = request.POST["c_message"]
   


    cust = Contact(name=n,email=e,Subject=s,Message=m)
    cust.save()

    return render(request, "contact.html")
