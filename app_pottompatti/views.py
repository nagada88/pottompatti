from django.shortcuts import render
from .models import *
from app_pottompatti.forms import ContactForm


def contact_context(request):
    """
    Globális context processor, amely a kapcsolati adatokat elküldi az összes view-ba.
    """
    return { 'kapcsolat': Kapcsolat.get_solo()}


# Create your views here.
def rolunk(request):
    return render(request, 'rolunk.html')

def tortak(request):
    tortacategories = ProductCategory.objects.filter(product_main_category="tortak")
    tortak = Product.objects.filter(product_category__product_main_category="tortak")

    return render(request, 'tortak.html', {'tortacategories': tortacategories, 'tortak': tortak})

def filter_cakes(request):
    category_ids = request.GET.getlist('torta_category')
    permanent_checked = request.GET.get('permanent')

    tortak = Product.objects.filter(product_category__product_main_category="tortak")

    if category_ids:
        tortak = tortak.filter(product_category__in=category_ids)

    if permanent_checked:
        tortak = tortak.filter(permanent=True)

    return render(request, 'partial_templates/cake_list.html', {'tortak': tortak})

def sutemenyek(request):
    sutemenycategories = ProductCategory.objects.filter(product_main_category="sutemenyek")
    sutemenyek = Product.objects.filter(product_category__product_main_category="sutemenyek")

    return render(request, 'sutemenyek.html', {'sutemenycategories': sutemenycategories, 'sutemenyek': sutemenyek})

def filter_sutemenyek(request):
    category_ids = request.GET.getlist('sutemeny_category') 
    permanent_checked = request.GET.get('permanent')
    
    sutemenyek = Product.objects.filter(product_category__product_main_category="sutemenyek")

    if category_ids:
        sutemenyek = sutemenyek.filter(product_category__in=category_ids)  # Csak a kiválasztott kategória tortái
    if permanent_checked:
        sutemenyek = sutemenyek.filter(permanent=True)


    return render(request, 'partial_templates/sutemeny_list.html', {'sutemenyek': sutemenyek})


def esemeny(request):
    return render(request, 'esemenyek.html', {})


def kapcsolat(request):
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

    return render(request, "kapcsolat.html", {'form': form, 'title': 'Pöttöm Patti kapcsolatfelvétel'})

def sikeresmail(request):
    return render(request, 'sikeresmail.html')