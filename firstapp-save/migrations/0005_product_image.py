# Generated by Django 2.2 on 2020-06-21 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_auto_20200621_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products_images'),
        ),
    ]
