# Generated by Django 3.0.8 on 2020-11-07 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_auto_20201107_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='is_archive',
            field=models.BooleanField(default=False),
        ),
    ]
