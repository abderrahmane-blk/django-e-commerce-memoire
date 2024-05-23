# Generated by Django 5.0.3 on 2024-05-23 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0026_alter_chargilypayment_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargilypayment',
            name='status',
            field=models.CharField(choices=[('progress', 'IN PROGRESS'), ('paid', 'PAID'), ('expired', 'EXPIRED'), ('canceled', 'CANCELED'), ('failed', 'FAILED')], default='progress', max_length=25),
        ),
    ]