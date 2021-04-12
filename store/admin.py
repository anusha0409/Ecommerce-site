from django.contrib import admin
from .models.product import Product
from .models.category import Categorie
from .models.customer import Customer


class AdminProduct(admin.ModelAdmin):
    list_display = ['name' ,'price' ,'category']


class AdminCategorie(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Categorie, AdminCategorie)
admin.site.register(Customer)