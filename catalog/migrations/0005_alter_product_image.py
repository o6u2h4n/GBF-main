# Generated by Django 4.1.3 on 2022-11-18 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, upload_to="catalog/static/img/"),
        ),
    ]
