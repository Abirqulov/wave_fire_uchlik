# Generated by Django 3.1.4 on 2021-03-29 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20210329_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uchlik',
            name='description',
        ),
        migrations.RemoveField(
            model_name='uchlik',
            name='name',
        ),
        migrations.AddField(
            model_name='uchlik',
            name='description_uz',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='uchlik',
            name='name_uz',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
