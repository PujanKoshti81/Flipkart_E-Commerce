# Generated by Django 2.2.1 on 2019-12-22 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flipmart', '0036_auto_20191222_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_details',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_history', to='E_Commerce.Basic_product_form'),
        ),
        migrations.AlterField(
            model_name='order_details',
            name='purchase_history_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_details', to='flipmart.purchase_history'),
        ),
    ]
