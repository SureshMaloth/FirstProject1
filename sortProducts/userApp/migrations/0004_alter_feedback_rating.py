# Generated by Django 5.0.1 on 2024-02-02 13:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0003_alter_product_category_delete_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=2, validators=[django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]
