# Generated by Django 3.1.1 on 2020-09-28 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("records", "0009_auto_20200928_2116"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="purchaserecord",
            name="implementation_location",
        ),
        migrations.AlterField(
            model_name="purchaserecord",
            name="order_amount_zar",
            field=models.DecimalField(
                blank=True, db_index=True, decimal_places=2, max_digits=20, null=True
            ),
        ),
    ]
