# Generated by Django 5.0.3 on 2024-05-04 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_promotiona_price_product_promotion_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='promotion_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, null=True),
        ),
    ]
