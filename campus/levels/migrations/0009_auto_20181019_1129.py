# Generated by Django 2.1.2 on 2018-10-19 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0008_auto_20181019_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_relation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ques', to='levels.Answer'),
        ),
    ]