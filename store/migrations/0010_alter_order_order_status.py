# Generated by Django 3.2 on 2021-04-17 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_rename_status_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('OrderPlaced', 'Order Placed'), ('OrderDispatched', 'Order Dispatched'), ('Intransit', 'In transit'), ('Delivered', 'Delivered')], default='Order Dispached', max_length=30),
        ),
    ]
