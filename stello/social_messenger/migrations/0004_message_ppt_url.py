# Generated by Django 3.0.8 on 2020-10-20 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_messenger', '0003_auto_20201015_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='ppt_url',
            field=models.URLField(blank=True, max_length=380, null=True),
        ),
    ]
