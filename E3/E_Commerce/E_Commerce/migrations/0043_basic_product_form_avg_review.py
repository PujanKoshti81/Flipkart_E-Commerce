# Generated by Django 2.2.1 on 2019-10-29 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Commerce', '0042_auto_20191024_0217'),
    ]

    operations = [
        migrations.AddField(
            model_name='basic_product_form',
            name='avg_review',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name='Review'),
        ),
    ]
