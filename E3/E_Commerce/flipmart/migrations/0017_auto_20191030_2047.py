# Generated by Django 2.2.1 on 2019-10-30 15:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flipmart', '0016_remove_user_delivery_address_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_delivery_address',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_delivery_address',
            name='time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
