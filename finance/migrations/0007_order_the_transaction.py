# Generated by Django 5.0.3 on 2024-05-13 22:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0006_alter_order_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='the_transaction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='finance.transaction'),
        ),
    ]