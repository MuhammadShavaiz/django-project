# Generated by Django 5.0.6 on 2024-06-23 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_shop', '0004_rename_prod_img_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]