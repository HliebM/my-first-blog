# Generated by Django 4.2.10 on 2024-02-15 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.BigIntegerField(default=0),
        ),
    ]
