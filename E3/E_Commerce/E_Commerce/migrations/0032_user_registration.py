# Generated by Django 2.2.1 on 2019-09-07 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Commerce', '0031_auto_20190813_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('email', models.CharField(max_length=30, verbose_name='email')),
                ('phone_no', models.CharField(max_length=15, verbose_name='phone_no')),
                ('password', models.CharField(max_length=15, verbose_name='password')),
                ('age', models.CharField(max_length=5, verbose_name='age')),
                ('gender', models.CharField(max_length=7, verbose_name='gender')),
            ],
        ),
    ]
