# Generated by Django 4.0.2 on 2022-02-25 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_university_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='latitude',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='university',
            name='longitude',
            field=models.CharField(default='', max_length=255),
        ),
    ]
