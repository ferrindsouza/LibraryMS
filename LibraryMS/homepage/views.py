from django.shortcuts import render 

# Create your views here.
from .models import Library


def homepage(request):
    imgs = Library.objects.all()
    return render(request, 'homepage.html', {'imgs': imgs})
