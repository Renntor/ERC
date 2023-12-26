from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Link(models.Model):

    choice = [
        ("FC", "factory"),
        ("RN", "retail network"),
        ("IE", "individual entrepreneur"),
    ]

    name = models.CharField(max_length=150, verbose_name='название')
    contact = models.CharField(max_length=200, verbose_name='контакт')
    email = models.EmailField(verbose_name='email')
    country = models.CharField(max_length=170, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город')
    street = models.CharField(max_length=100, verbose_name='улица')
    number = models.CharField(max_length=10, verbose_name='номер')
    house = models.CharField(max_length=50, verbose_name='дом')
    debt = models.FloatField(default=0, verbose_name='долг')
    create = models.DateTimeField(auto_now=True, verbose_name='время создания')
    structure = models.CharField(max_length=2, choices=choice, verbose_name='структура')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='владелец')

    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='поставщик')

    def __str__(self):
        return f'{self.name}, {self.email}, {self.contact}'

    class Meta:
        verbose_name = 'звено'
        verbose_name_plural = 'звенья'
