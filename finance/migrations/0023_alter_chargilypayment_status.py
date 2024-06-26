# Generated by Django 5.0.3 on 2024-05-22 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0022_alter_chargilypayment_status_alter_transaction_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargilypayment',
            name='status',
            field=models.CharField(choices=[('failed', 'FAILED'), ('progress', 'IN PROGRESS'), ('canceled', 'CANCELED'), ('paid', 'PAID'), ('expired', 'EXPIRED')], default='progress', max_length=25),
        ),
    ]
