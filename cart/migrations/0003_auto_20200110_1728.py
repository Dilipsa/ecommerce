# Generated by Django 3.0.1 on 2020-01-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20200110_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='number',
            field=models.IntegerField(),
        ),
    ]
