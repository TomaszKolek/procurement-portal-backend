# Generated by Django 3.1.1 on 2020-10-17 12:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0016_auto_20201012_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaserecord',
            name='buyer_name',
            field=models.CharField(db_index=True, max_length=500, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='purchaserecord',
            name='supplier_name',
            field=models.CharField(db_index=True, max_length=500, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]