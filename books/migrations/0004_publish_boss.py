# Generated by Django 2.2.1 on 2019-05-23 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20190523_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='publish',
            name='boss',
            field=models.CharField(default='', max_length=100, verbose_name='老板名字'),
        ),
    ]