# Generated by Django 4.2.10 on 2024-02-14 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
