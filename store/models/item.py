from django.db import models
from .category import Categorie
from .customer import Customer


class Item(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Categorie ,on_delete=models.CASCADE, default=1)
    description=models.CharField(max_length=200 , default='Description not available' , null=True , blank=True)
    image=models.ImageField(upload_to='media/')
    quantity=models.IntegerField(default=10)
    seller = models.ForeignKey(Customer,on_delete=models.CASCADE,default=None)


    @staticmethod
    def get_items_by_id(ids):
        return Item.objects.filter(id__in =ids)


    @staticmethod
    def gete_all_item():
        return Item.objects.all()

    @staticmethod
    def get_all_items_by_categoryid(category_id):
        if category_id:
            return Item.objects.filter(category= category_id)
        else:
            return Item.gete_all_products()

    def save_item(self):
        self.save()

    @staticmethod
    def get_items_by_seller(customer_id):
        return item.objects.filter(seller=customer_id)