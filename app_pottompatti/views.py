from django.shortcuts import render
from .models import *

# Create your views here.
def rolunk(request):
    hirek = Hirek.objects.filter().order_by('-id')[:3]
    terjbe = TerjBeHozzank.objects.get(id=1)

    return render(request, 'rolunk.html', {'hirek': hirek, 'terjbe': terjbe})

def uzletunk(request):
    return render(request, 'uzletunk.html')

def tortak(request):
    tortacategories = ProductCategory.objects.filter(product_main_category="Torták")
    tortak = Product.objects.filter(product_category__product_main_category="Torták")
    return render(request, 'tortak.html', {'tortacategories': tortacategories, 'tortak': tortak})

def sutemeny(request):
    sutemenycategories = ProductCategory.objects.filter(product_main_category="Sütemények")
    return render(request, 'sutemeny.html', {'sutemenycategories': sutemenycategories})

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