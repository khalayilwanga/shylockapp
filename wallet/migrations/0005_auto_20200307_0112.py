# Generated by Django 3.0.3 on 2020-03-06 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_auto_20200306_1827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shylockentry',
            old_name='type',
            new_name='type_choice',
        ),
    ]
