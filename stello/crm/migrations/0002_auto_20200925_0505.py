# Generated by Django 3.0.8 on 2020-09-25 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integration',
            name='avatar',
            field=models.URLField(blank=True, max_length=380, null=True),
        ),
    ]
