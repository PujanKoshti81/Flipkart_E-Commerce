# Generated by Django 2.2.1 on 2019-07-16 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Commerce', '0017_banners_image_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banners_image',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
