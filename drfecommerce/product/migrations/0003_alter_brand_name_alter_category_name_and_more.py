# Generated by Django 4.2.7 on 2023-11-15 18:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_remove_product_lokesh"),
    ]

    operations = [
        migrations.AlterField(
            model_name="brand",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]