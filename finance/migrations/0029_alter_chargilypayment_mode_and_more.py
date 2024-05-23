# Generated by Django 5.0.3 on 2024-05-23 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0028_alter_chargilypayment_mode_and_more'),
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
            field=models.CharField(choices=[('progress', 'IN PROGRESS'), ('expired', 'EXPIRED'), ('paid', 'PAID'), ('canceled', 'CANCELED'), ('failed', 'FAILED')], default='progress', max_length=25),
        ),
        migrations.AlterField(
            model_name='order',
            name='price_paid',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
