from django.db import models


class Link(models.Model):
    name = models.CharField(max_length=150, verbose_name='название')
    contact = models.CharField(max_length=200, verbose_name='контакт')
    email = models.EmailField(verbose_name='email')
    country = models.CharField(max_length=170, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город')
    street = models.CharField(max_length=100, verbose_name='улица')
    number = models.CharField(max_length=10, verbose_name='номер')
    house = models.CharField(max_length=50, verbose_name='дом')
