# Generated by Django 3.0.3 on 2020-03-08 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0008_auto_20200308_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shylockentry',
            name='deadline',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='shylockentry',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]