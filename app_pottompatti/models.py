from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django_quill.fields import QuillField
from django.core.exceptions import ValidationError
import os
from solo.models import SingletonModel

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
   
class CategoryChoices(models.TextChoices):
    TORTAK = 'tortak', 'Torták'
    SUTEMENYEK = 'sutemenyek', 'Sütemények'
    
class ProductCategory(models.Model):
    product_main_category = models.CharField(max_length=10, choices=CategoryChoices.choices, default='tortak', verbose_name = 'főkategória')
    name = models.CharField(max_length=200, verbose_name="termék kategória")

    class Meta:
        verbose_name = 'kategória'
        verbose_name_plural = 'kategóriák'

    def __str__(self):
        return self.name

class Product(ImageHandlerMixin, models.Model):
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name="kategória")
    name = models.CharField(max_length=200, verbose_name="név", default="termek")
    description = models.TextField(max_length=300, verbose_name="termék leírás", default="leírás később érkezik")
    photo = models.ImageField(upload_to='app_pottompatti/img/photos/', verbose_name = "kép", default="/app_pottompatti/img/bakery.jpg")
    photo_tumb = models.ImageField(upload_to='app_pottompatti/img/thumbs/', editable=False) 
    permanent = models.BooleanField(default=True, verbose_name="állandó kínálat")

    class Meta:
        verbose_name = 'termék'
        verbose_name_plural = 'termékek'

    def __str__(self):
        return self.name
    
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
    

class Kapcsolat(SingletonModel):
    nyitvatartas=models.CharField(max_length=50, verbose_name="nyitvatartás")
    emailcim=models.CharField(max_length=50, default="", verbose_name="email cím")
    address=models.CharField(max_length=50, default="", verbose_name="cím")
    addresslink=models.CharField(max_length=50, default="", verbose_name="google térkép link")
    facebook=models.CharField(max_length=100, default="", verbose_name="facebook link")
    instagram=models.CharField(max_length=100, default="", verbose_name="instagram link")
    tiktok=models.CharField(max_length=100, default="", verbose_name="tiktok link")
    telefonszam=models.CharField(max_length=50, default="", verbose_name="telefonszám")

    class Meta:
        verbose_name = 'Kapcsolati adatok'

    def __str__(self):
        return "Kapcsolat"
    

class TortaKepek(ImageHandlerMixin, models.Model):
    photo = models.ImageField(upload_to='app_pottompatti/img/photos/', verbose_name = "kép", default="/app_pottompatti/img/bakery.jpg")
    photo_tumb = models.ImageField(upload_to='app_pottompatti/img/thumbs/', editable=False) 

    class Meta:
        verbose_name = 'torta kép'
        verbose_name_plural = 'torta képek'


    def __str__(self):
        return "torta kép " + str(self.pk)