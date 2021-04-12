from django.contrib.auth.models import Group

customer_group, created = Group.objects.get_or_create(name='Customer')
retailer_group, created = Group.objects.get_or_create(name='Retailer')
wholesaler_group, created = Group.objects.get_or_create(name='Wholesaler')

customer_group.permissions.set([permission_list])

doctor_group.user_set.add(user)
            OR
user.groups.add(doctor_group)

#Check user in the group
def is_doctor(user):
    return user.groups.filter(name='Doctor').exists()
from django.contrib.auth.decorators import user_passes_test
@user_passes_test(is_doctor)
def my_view(request):
    pass
 
