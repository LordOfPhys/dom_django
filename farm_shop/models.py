from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'user')
    first_name = models.CharField(max_length=30, default='Имя')
    last_name = models.CharField(max_length=30, default='Фамилия')
    phone = models.CharField(max_length=20, default='0')
    adress = models.CharField(max_length=100, default='Адрес')
    FIRM_TYPE_CHOICES = (('F', 'Физическое лицо'), ('U', 'Юридическое лицо'))
    firm_type = models.CharField(max_length=1, choices=FIRM_TYPE_CHOICES, default='')
    photo = models.ImageField(upload_to='people_photos/', default='user_icon.png')
    rating = models.IntegerField(default='5')

    def set_profile(self, first_name, last_name, phone, adress, firm_type, photo):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.adress = adress
        self.firm_type = firm_type
        self.photo = photo
        self.save()

    def get_user(self):
        return self.user

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, f_name):
        self.first_name = f_name
        self.save()

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, l_name):
        self.last_name = l_name
        self.save()

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone
        self.save()

    def get_adress(self):
        return self.adress

    def set_adres(self, adress):
        self.adress = adress
        self.save()

    def get_firm_type(self):
        return self.firm_type

    def set_firm_type(self, f_type):
        self.firm_type = f_type
        self.save()

    def get_photo(self):
        return self.photo

    def set_photo(self, photo):
        self.photo = photo
        self.save()

    def get_rating(self):
        return self.rating

    def set_rating(self, rating):
        self.rating = rating
        self.save()

    def __str__(self):
        return self.phone

class Category(models.Model):
    label = models.CharField(max_length=100, default='Другое')

    def __str__(self):
        return self.label

class ItemProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_type = models.ForeignKey(Category, on_delete=models.CASCADE)
    label = models.CharField(max_length=100, default='Название товара', unique=True)
    image = models.ImageField(upload_to='item_image/', default='')
    price = models.FloatField(default=0)
    description = models.TextField(default='Описание товара')

    def __str__(self):
        return self.label

    def get_label(self):
        return self.label

    def get_user(self):
        return self.user

    def get_image(self):
        return self.image

    def get_price(self):
        return self.price

class ItemNews(models.Model):
    label = models.CharField(max_length=100, default='Заголовок', unique=True)
    prev = models.CharField(max_length=500, default='Краткое описание')
    description = models.TextField(default='Новость целиком')
    image = models.ImageField(upload_to='item_news/', null=True, default='', blank=True)
    date = models.DateField()

    def set_image(self, image):
        self.image = image
        self.save()

    def get_prev(self):
        return self.prev

    def get_description(self):
        return self.description

    def get_label(self):
        return self.label

    def get_date(self):
        return self.date

    def get_image(self):
        return self.image

    def __str__(self):
        return self.label