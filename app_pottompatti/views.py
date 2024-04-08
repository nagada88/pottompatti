from django.shortcuts import render
from .models import *

# Create your views here.
def rolunk(request):
    rolunk = Bemutatkozas.objects.get(id=1)
    terjbe = TerjBeHozzank.objects.get(id=1)

    return render(request, 'rolunk.html', {'rolunk': rolunk, 'bemutatkozas': rolunk, 'terjbe': terjbe})

def uzletunk(request):
    return render(request, 'uzletunk.html')

def kinalat(request):
    productmaincategories = ProductMainCategory.objects.all()
    return render(request, 'kinalat.html', {'productmaincategories': productmaincategories})

def eskuvo(request):
    return render(request, 'eskuvo.html')

def rendezvenyek(request):
    return render(request, 'rendezvenyek.html')

def esemenyek(request):
    return render(request, 'esemenyek.html')

def karrier(request):
    return render(request, 'karrier.html')

def kapcsolat(request):
    return render(request, 'kapcsolat.html')

def sikeresmail(request):
    return render(request, 'sikeresmail.html')