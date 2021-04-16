from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django_google_maps import fields as map_fields
from geoposition import Geoposition
from geoposition.fields import GeopositionField

    

class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    phone= models.CharField(max_length=10)
    email= models.EmailField()
    password=models.CharField(max_length=500)
    location=models.CharField(max_length=500)
    group_name=models.CharField(max_length=500)
    #address = map_fields.AddressField(max_length=200)
    #geolocation = map_fields.GeoLocationField(max_length=100)
    #position = GeopositionField(default=Geoposition(40.77, 73.98))
    latitude= models.CharField(max_length=100,default="")
    longitude= models.CharField(max_length=100,default="")

    def register(self):
        username1=self.first_name+ " "+self.last_name+"101"
        user = User.objects.create_user(
        username = username1,
        password = self.password,
        email = self.email)
        user.save()
        my_group1 = Group.objects.get(name=self.group_name) 
        print(my_group1)
        my_group1.user_set.add(user)
        print("added " , self.first_name, " to", my_group1)

        #print(self.email)
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False


    @staticmethod
    def get_customer_by_id(ids):
        try:
            return Customer.objects.get(id__in= ids)
        except:
            return False

    @staticmethod
    def get_customer_by_role(group_name):
        return Customer.objects.filter(group_name = group_name)

    




