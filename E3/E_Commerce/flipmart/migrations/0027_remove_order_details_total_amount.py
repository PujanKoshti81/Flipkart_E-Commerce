# Generated by Django 2.2.1 on 2019-10-31 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flipmart', '0026_auto_20191031_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_details',
            name='total_amount',
        ),
    ]
