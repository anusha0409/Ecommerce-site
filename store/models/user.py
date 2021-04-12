from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
   
    is_customer = models.BooleanField( "Customer status",default=False)
    is_wholesaler = models.BooleanField("Retailer status",default=False)
    is_retailer = models.BooleanField("Wholesaler status" ,default=False)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name=  models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    
 #buyer=1
    #retailer=2
    #wholesaler=3

    #ROLE_CHOICES = (
        #(buyer ,"Customer"),
        #(retailer , "Retailer"),
        #(wholesaler, "Wholesaler"))
    #role=models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)