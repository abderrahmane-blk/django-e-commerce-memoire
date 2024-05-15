# Generated by Django 5.0.3 on 2024-05-13 22:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_rename_price_order_price_paid_order_quantity'),
        ('store', '0012_delete_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.store'),
        ),
    ]
