# Generated by Django 3.2.25 on 2024-05-01 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='product_size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]