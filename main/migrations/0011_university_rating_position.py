# Generated by Django 4.0.2 on 2022-02-26 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_purchase_purchase_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='rating_position',
            field=models.IntegerField(default=0),
        ),
    ]
