# Generated by Django 2.2.1 on 2019-07-13 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Commerce', '0010_product_details_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banners_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banner_image/')),
            ],
        ),
        migrations.AlterField(
            model_name='product_details',
            name='image',
            field=models.FileField(upload_to='product_images/'),
        ),
    ]
