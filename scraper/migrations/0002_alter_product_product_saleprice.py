# Generated by Django 4.0.6 on 2022-07-12 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_salePrice',
            field=models.FloatField(default=None),
        ),
    ]