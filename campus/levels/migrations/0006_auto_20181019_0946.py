# Generated by Django 2.1.2 on 2018-10-19 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0005_auto_20181019_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.ImageField(upload_to='images'),
        ),
    ]