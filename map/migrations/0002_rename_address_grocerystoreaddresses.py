# Generated by Django 4.1.1 on 2022-10-22 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Address',
            new_name='GroceryStoreAddresses',
        ),
    ]
