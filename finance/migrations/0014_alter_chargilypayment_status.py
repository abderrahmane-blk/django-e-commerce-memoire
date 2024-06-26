# Generated by Django 5.0.3 on 2024-05-18 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0013_alter_chargilypayment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargilypayment',
            name='status',
            field=models.CharField(choices=[('expired', 'EXPIRED'), ('failed', 'FAILED'), ('canceled', 'CANCELED'), ('progress', 'IN PROGRESS'), ('paid', 'PAID')], default='progress', max_length=25),
        ),
    ]
