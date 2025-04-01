from django.shortcuts import render
from .models import *
from app_pottompatti.forms import ContactForm

# Create your views here.
def rolunk(request):
    hirek = Hirek.objects.filter().order_by('-id')[:3]
    terjbe = TerjBeHozzank.objects.get(id=1)
    kapcsolat = Kapcsolat.objects.get(id=1)

    return render(request, 'rolunk.html', {'hirek': hirek, 'terjbe': terjbe, 'kapcsolat': kapcsolat})

def uzletunk(request):
    return render(request, 'uzletunk.html')

def tortak(request):
    tortacategories = ProductCategory.objects.filter(product_main_category="Torták")
    tortak = Product.objects.filter(product_category__product_main_category="Torták")
    kapcsolat = Kapcsolat.objects.get(id=1)
    return render(request, 'tortak.html', {'tortacategories': tortacategories, 'tortak': tortak, 'kapcsolat': kapcsolat})

def filter_cakes(request):
    category_ids = request.GET.getlist('torta_category') 
    Cake = Product.objects.filter(product_category__product_main_category="Torták")
    if category_ids:
        tortak = Cake.filter(product_category__in=category_ids)  # Csak a kiválasztott kategória tortái
    else:
        tortak = Cake  # Ha nincs kiválasztott kategória, minden tortát visszaadunk

    return render(request, 'partial_templates/cake_list.html', {'tortak': tortak})

def sutemenyek(request):
    kapcsolat = Kapcsolat.objects.get(id=1)
    sutemenycategories = ProductCategory.objects.filter(product_main_category="Sütemények")
    sutemenyek = Product.objects.filter(product_category__product_main_category="Sütemények")
    kapcsolat = Kapcsolat.objects.get(id=1)
    return render(request, 'sutemenyek.html', {'sutemenycategories': sutemenycategories, 'sutemenyek': sutemenyek, 'kapcsolat': kapcsolat})

def filter_sutemenyek(request):
    category_ids = request.GET.getlist('sutemeny_category') 
    Suti = Product.objects.filter(product_category__product_main_category="Sütemények")
    if category_ids:
        sutemenyek = Suti.filter(product_category__in=category_ids)  # Csak a kiválasztott kategória tortái
    else:
        sutemenyek = Suti  # Ha nincs kiválasztott kategória, minden tortát visszaadunk

    return render(request, 'partial_templates/sutemeny_list.html', {'sutemenyek': sutemenyek})


def esemeny(request):
    return render(request, 'esemenyek.html', {})


def kapcsolat(request):
    kapcsolat = Kapcsolat.objects.get(id=1)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "pottompatti.hu - érdeklődés"
            body = {
                'név': 'Feladó: ' + form.cleaned_data['name'],
                'email cím': form.cleaned_data['email_address'],
                'üzenet': form.cleaned_data['message'],
            }
            message = "Üzenet érkezett a Pöttöm Patti honlapról: \n\n" + "\n".join(body.values())

            try:
                send_mail(subject, message,  body['email cím'], [kapcsolat.emailcim])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("rolunk.html")
        else:
            messages.error(request, form.errors)
    else:
        form = ContactForm()

    return render(request, "kapcsolat.html", {'form': form, 'title': 'Pöttöm Patti kapcsolatfelvétel', 'kapcsolat': kapcsolat })

def sikeresmail(request):
    return render(request, 'sikeresmail.html')