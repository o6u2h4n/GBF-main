# Generated by Django 4.1.3 on 2022-11-18 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_alter_category_options_alter_product_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, upload_to="products/"),
        ),
    ]