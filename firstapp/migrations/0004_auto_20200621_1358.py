# Generated by Django 2.2 on 2020-06-21 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productcategory',
            old_name='discription',
            new_name='description',
        ),
    ]
