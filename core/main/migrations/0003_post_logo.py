# Generated by Django 5.0.4 on 2024-04-29 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='logo',
            field=models.ImageField(max_length=250, null=True, upload_to=''),
        ),
    ]
