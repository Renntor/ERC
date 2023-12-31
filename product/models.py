from django.db import models
from link.models import Link, NULLABLE


class Product(models.Model):
    link = models.ForeignKey(Link, on_delete=models.SET_NULL, verbose_name='компания', **NULLABLE)
    name = models.CharField(max_length=100, verbose_name='название')
    model = models.CharField(max_length=100, verbose_name='модель')
    release_date = models.DateField(verbose_name='дата выхода')

    def __str__(self):
        return f'{self.name}, {self.model}, {self.release_date}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
