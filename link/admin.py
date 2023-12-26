from django.contrib import admin
from link.models import Link
from django.urls import reverse


@admin.action(description="Обнуление задолженности")
def debt_nullification(modeladmin, request, queryset):
    queryset.update(debt=0.0)


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'street', 'number', 'house', 'debt', 'create', 'supplier')
    list_filter = ('city',)
    actions = [debt_nullification]

