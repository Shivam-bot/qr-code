import re
from django.shortcuts import render,redirect
from .models import user_detail
# Create your views here.


def home_view(request):
    context = {'data':user_detail.objects.all()}
    return render(request,'homepage.html',context)

def user_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        user_detail.objects.create(name=name, dob=dob)
        return redirect('home-view')
    return render(request,'register.html')
