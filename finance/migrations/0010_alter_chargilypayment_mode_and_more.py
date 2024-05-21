# Generated by Django 5.0.3 on 2024-05-17 00:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0009_alter_chargilypayment_mode_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargilypayment',
            name='mode',
            field=models.CharField(choices=[('CIB', 'CIB'), ('EDAHABIA', 'EDAHABIA')], default='EDAHABIA', max_length=25),
        ),
        migrations.AlterField(
            model_name='chargilypayment',
            name='status',
            field=models.CharField(choices=[('failed', 'FAILED'), ('paid', 'PAID'), ('canceled', 'CANCELED'), ('expired', 'EXPIRED'), ('progress', 'IN PROGRESS')], default='progress', max_length=25),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]