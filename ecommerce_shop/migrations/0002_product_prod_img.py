# Generated by Django 5.0.6 on 2024-06-14 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prod_img',
            field=models.ImageField(default='', upload_to='ecommerce_shop/images'),
        ),
    ]
