from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django_quill.fields import QuillField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
import os

# Create your models here.

class ImageHandlerMixin():
    def save(self, *args, **kwargs):
        if not self.photo.closed:
            if not self.make_thumbnail():
                # set to a default thumbnail
                raise Exception('Could not create thumbnail - is the file type valid?')

        super(ImageHandlerMixin, self).save(*args, **kwargs)


    def make_thumbnail(self):

        image = Image.open(self.photo)
        image.thumbnail((1000,1000), Image.BICUBIC)

        thumb_name, thumb_extension = os.path.splitext(self.photo.name)
        thumb_extension = thumb_extension.lower()

        thumb_filename = thumb_name + '_thumb' + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False  # Unrecognized file type

        # Save thumbnail to in-memory file as StringIO
        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        # set save=False, otherwise it will run in an infinite loop
        self.photo_tumb.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()

        return True   



class Hirek(ImageHandlerMixin, models.Model):
    title=models.CharField(max_length=200, verbose_name="Hír cím")
    content=QuillField(max_length=1000, verbose_name = "Hír szövege")
    photo = models.ImageField(upload_to='app_pottompatti/img/photos/', verbose_name = "kép", default="/app_pottompatti/img/bakery.jpg")
    photo_tumb = models.ImageField(upload_to='app_pottompatti/img/thumbs/', editable=False) 

    # def save(self, *args, **kwargs):
    #     if not self.pk and Bemutatkozas.objects.exists():
    #     # if you'll not check for self.pk 
    #     # then error will also be raised in the update of exists model
    #         raise ValidationError('Csak egy bemutatkozas bejegyzes lehet')
    #     return super(Hirek, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Hír'
        verbose_name_plural = 'Hírek'

    def __str__(self):
        return self.title

class TerjBeHozzank(models.Model):
    content=QuillField(verbose_name = "Bemutatkozó szöveg")

    def save(self, *args, **kwargs):
        if not self.pk and TerjBeHozzank.objects.exists():
        # if you'll not check for self.pk 
        # then error will also be raised in the update of exists model
            raise ValidationError('Csak egy térj be hozzánk szöveg lehet bejegyzes lehet')
        return super(TerjBeHozzank, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Térj Be Hozzánk Szöveg'
        verbose_name_plural = 'Térj Be Hozzánk Szöveg'

    def __str__(self):
        return "Térj Be Hozzánk Szöveg"
    
class CategoryChoices(models.TextChoices):
    tortak = "Torták"
    sutemenyek = "Sütemények"
    
class ProductCategory(models.Model):
    product_main_category = models.CharField(max_length=10, choices=CategoryChoices.choices, default='tortak', verbose_name = 'főkategória')
    name = models.CharField(max_length=200, verbose_name="termék kategória")
    priority = models.IntegerField(default=10, verbose_name="sorrend", validators=[MaxValueValidator(10), MinValueValidator(1)])

    class Meta:
        verbose_name = 'kategória'
        verbose_name_plural = 'kategóriák'

    def __str__(self):
        return self.name

class Product(ImageHandlerMixin, models.Model):
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name="név", default="termek")
    description = models.TextField(max_length=300, verbose_name="termék leírás", default="leírás később érkezik")
    photo = models.ImageField(upload_to='app_pottompatti/img/photos/', verbose_name = "kép", default="/app_pottompatti/img/bakery.jpg")
    photo_tumb = models.ImageField(upload_to='app_pottompatti/img/thumbs/', editable=False) 
    
    class Meta:
        verbose_name = 'termék'
        verbose_name_plural = 'termékek'

    def __str__(self):
        return self.name
    
class AllasLehetoseg(models.Model):
    content=QuillField(verbose_name = "Álláslehetőség")
    
    class Meta:
        verbose_name = 'Álláslehetőség'
        verbose_name_plural = 'Álláslehetőségek'

    def __str__(self):
        return "álláslehetőség"
    

class Eskuvo(models.Model):
    eskuvo_szoveg=QuillField(verbose_name = "Esküvő szöveg")

    def save(self, *args, **kwargs):
        if not self.pk and Eskuvo.objects.exists():
        # if you'll not check for self.pk 
        # then error will also be raised in the update of exists model
            raise ValidationError('Csak egy esküvői bemutatkozó szöveg lehet bejegyzes lehet')
        return super(Eskuvo, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Esküvő szöveg'
        verbose_name_plural = 'Esküvő szöveg'

    def __str__(self):
        return "esküvő szöveg"
    
class EskuvoKerdezzFelelek(models.Model):
    eskuvo_kerdes=models.TextField(max_length=300, verbose_name="kérdés", default="")
    eskuvo_valasz=models.TextField(max_length=300, verbose_name="válasz", default="")
    
    class Meta:
        verbose_name = 'Esküvő kérdezz felelek'
        verbose_name_plural = 'Esküvő kérdezz felelek objektumok'

    def __str__(self):
        return self.eskuvo_kerdes
    
class Rendezveny(models.Model):
    rendezveny_szoveg=QuillField(verbose_name = "Rendezvény szöveg")

    def save(self, *args, **kwargs):
        if not self.pk and Rendezveny.objects.exists():
        # if you'll not check for self.pk 
        # then error will also be raised in the update of exists model
            raise ValidationError('Csak egy rendezvény bemutatkozó szöveg lehet bejegyzes lehet')
        return super(Rendezveny, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Rendezvény szöveg'
        verbose_name_plural = 'Rendezvény szöveg'

    def __str__(self):
        return "rendezvény szöveg"
    
class RendezvenyKerdezzFelelek(models.Model):
    rendezveny_kerdes=models.TextField(max_length=300, verbose_name="kérdés", default="")
    rendezveny_valasz=models.TextField(max_length=300, verbose_name="válasz", default="")
    
    class Meta:
        verbose_name = 'Rendezvény kérdezz felelek'
        verbose_name_plural = 'Rendezvény kérdezz felelek objektumok'

    def __str__(self):
        return self.rendezveny_kerdes
    
class Kapcsolat(models.Model):
    nyitvatartas=models.CharField(max_length=50, verbose_name="nyitvatartás")
    emailcim=models.CharField(max_length=50, default="", verbose_name="email cím")
    adress=models.CharField(max_length=50, default="", verbose_name="cím")
    adresslink=models.CharField(max_length=50, default="", verbose_name="google térkép link")
    facebook=models.CharField(max_length=50, default="", verbose_name="facebook link")
    telefonszam=models.CharField(max_length=50, default="", verbose_name="telefonszám")

    class Meta:
        verbose_name = 'Kapcsolat'
        verbose_name_plural = 'Kapcsolat'

    def __str__(self):
        return "Kapcsolat"
    
class Karrier(models.Model):
    karrier=QuillField(verbose_name = "Karrier szöveg")

    def save(self, *args, **kwargs):
        if not self.pk and Karrier.objects.exists():
        # if you'll not check for self.pk 
        # then error will also be raised in the update of exists model
            raise ValidationError('Csak egy karrier szöveg lehet bejegyzes lehet')
        return super(Karrier, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Karrier szöveg'
        verbose_name_plural = 'Karrier szöveg'

    def __str__(self):
        return "karrier szöveg"
    
# class ProductMainImg(ImageHandlerMixin, models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     photo = models.ImageField(upload_to='app_pottompatti/img/photos/', verbose_name = "kiemelt kép")
#     photo_tumb = models.ImageField(upload_to='app_menhely/img/thumbs/', editable=False) 
    
#     class Meta:
#         verbose_name = 'kiemelt kép'
#         verbose_name_plural = 'kiemelt képek'

#     def __str__(self):
#         return "kép"