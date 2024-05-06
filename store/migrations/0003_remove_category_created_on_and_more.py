# Generated by Django 5.0.3 on 2024-05-03 16:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_cart_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='category',
            name='updated_on',
        ),
        migrations.AddField(
            model_name='product',
            name='promotion',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='cart_item',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]