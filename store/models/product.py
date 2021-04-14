from django.db import models
from .category import Categorie


class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Categorie ,on_delete=models.CASCADE, default=1)
    description=models.CharField(max_length=200 , default='Description not available' , null=True , blank=True)
    image=models.ImageField(upload_to='media/')


    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)


    @staticmethod
    def gete_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category= category_id)
        else:
            return Product.gete_all_products()