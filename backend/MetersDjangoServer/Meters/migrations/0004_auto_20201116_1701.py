# Generated by Django 2.2.17 on 2020-11-16 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Meters', '0003_auto_20201116_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meter',
            old_name='user',
            new_name='User',
        ),
    ]
