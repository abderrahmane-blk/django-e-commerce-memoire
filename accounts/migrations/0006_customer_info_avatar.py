# Generated by Django 5.0.3 on 2024-05-18 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_customer_info_customer_specific_property_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_info',
            name='avatar',
            field=models.ImageField(null=True, upload_to='users'),
        ),
    ]