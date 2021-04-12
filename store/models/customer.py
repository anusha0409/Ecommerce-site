from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    phone= models.CharField(max_length=10)
    email= models.EmailField()
    password=models.CharField(max_length=500)
    location=models.CharField(max_length=500)
    group_name=models.CharField(max_length=500)

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

