# Generated by Django 3.0.8 on 2020-10-21 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_messenger', '0006_message_unread_messages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='unread_messages',
        ),
    ]
