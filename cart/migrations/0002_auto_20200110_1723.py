# Generated by Django 3.0.1 on 2020-01-10 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cloth_name',
            field=models.CharField(default='leggings', max_length=20),
        ),
        migrations.AddField(
            model_name='cart',
            name='new',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='number',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cloth_color',
            field=models.CharField(choices=[('GREY', 'Grey'), ('BLACK', 'Black'), ('YELLOW', 'Yellow'), ('RED', 'Red'), ('WHITE', 'White'), ('GREEN', 'Green'), ('ORANGE', 'Orange'), ('BLUE', 'Blue'), ('BROWN', 'Brown'), ('PINK', 'Pink')], default='RED', max_length=10),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cloth_size',
            field=models.CharField(choices=[('SMALL', 'Small'), ('MEDIUM', 'Medim'), ('LARGE', 'LARGE'), ('X LARGEL', 'X-large'), ('XX LARGE', 'XX-large')], default='SMALL', max_length=10),
        ),
    ]
