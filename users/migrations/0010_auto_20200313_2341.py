# Generated by Django 3.0.3 on 2020-03-13 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200313_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='Your name', max_length=70),
        ),
    ]
