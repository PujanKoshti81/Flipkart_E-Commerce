# Generated by Django 2.2.1 on 2019-07-13 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Commerce', '0012_auto_20190713_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_details',
            name='image',
            field=models.FileField(upload_to='product_images'),
        ),
    ]
