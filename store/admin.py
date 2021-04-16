from django.contrib import admin
from .models.product import Product
from .models.category import Categorie
from .models.customer import Customer
from .models.orders import Order
from .models.item import Item

class AdminProduct(admin.ModelAdmin):
    list_display = ['name' ,'price' ,'category']

class AdminItem(admin.ModelAdmin):
    list_display = ['name' ,'price' ,'category']

class AdminCategorie(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Item, AdminItem)
admin.site.register(Categorie, AdminCategorie)
admin.site.register(Customer)
admin.site.register(Order)