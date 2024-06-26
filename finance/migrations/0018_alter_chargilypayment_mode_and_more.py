# Generated by Django 5.0.3 on 2024-05-18 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0017_alter_chargilypayment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargilypayment',
            name='mode',
            field=models.CharField(choices=[('EDAHABIA', 'EDAHABIA'), ('CIB', 'CIB')], default='EDAHABIA', max_length=25),
        ),
        migrations.AlterField(
            model_name='chargilypayment',
            name='status',
            field=models.CharField(choices=[('failed', 'FAILED'), ('paid', 'PAID'), ('expired', 'EXPIRED'), ('canceled', 'CANCELED'), ('progress', 'IN PROGRESS')], default='progress', max_length=25),
        ),
    ]
