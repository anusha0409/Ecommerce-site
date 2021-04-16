from django.db import models
from .category import Categorie
from .customer import Customer


class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Categorie ,on_delete=models.CASCADE, default=1)
    description=models.CharField(max_length=200 , default='Description not available' , null=True , blank=True)
    image=models.ImageField(upload_to='media/')
    quantity=models.IntegerField(default=10)
    seller = models.ForeignKey(Customer,on_delete=models.CASCADE,default=None)


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

    def save_product(self):
        self.save()

    @staticmethod
    def get_products_by_seller(customer_id):
        return Product.objects.filter(seller=customer_id)
    
    @staticmethod
    def get_all_products_by_roleOfSeller(group_name):
        products=Product.gete_all_products()
        data = []
        for product in products:
            seller_id=product.seller.id
            #print(seller_id)
            obj = Customer.objects.get(id=seller_id)
            if(obj.group_name== group_name):
                data.append(product)
        sellers=Customer.get_customer_by_role(group_name)
        return data
    
    @staticmethod
    def get_by_category_and_role(group_name, category_id):
        products= Product.get_all_products_by_categoryid(category_id)
        print(products)
        data = []
        for product in products:
            seller_id=product.seller.id
            obj = Customer.objects.get(id=seller_id)
            if(obj.group_name== group_name):
                data.append(product)
        sellers=Customer.get_customer_by_role(group_name)
        return data
