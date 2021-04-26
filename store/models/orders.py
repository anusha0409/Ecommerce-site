from django.db import models
from .product import Product
from .customer import Customer
import datetime




class Order(models.Model):
    status_choices = (('Order Placed','Order Placed'),('Order Dispatched', 'Order Dispatched'),('In transit','In transit'),('Delivered','Delivered'))
    mode_choices=(
    ('Online' ,'Online'),
    ('Offline' , 'Offline'))

    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    date_of_delivery=models.DateField(default=datetime.datetime.today)
    time_pickup=models.TimeField( default=datetime.time(16, 00), blank=True)
    delivery_person_details=models.CharField(max_length=100, default='', blank=True)
    order_status = models.CharField(max_length=30, default='Order Placed')
    mode=models.CharField(max_length=10, choices=mode_choices, default='Online')
    feedback=models.CharField(max_length=400,default="")

    def placeOrder(self):
        self.save()

    @staticmethod
    def gete_all_orders():
        return Order.objects.all().order_by('-date')

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

    @staticmethod
    def get_orders_by_seller(customer_id):
        data = []
        orders=Order.gete_all_orders()
        for order in orders:
            product_id=order.product.id
            #print(product_id)
            obj = Product.objects.get(id=product_id)
            #print(obj)
            if(obj.seller.id == customer_id):
                data.append(order)
        return data

    
