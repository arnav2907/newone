# Generated by Django 2.1.2 on 2018-10-17 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.CharField(max_length=100),
        ),
    ]