# Generated by Django 5.1.5 on 2025-02-23 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0003_author_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.ImageField(blank=True, default='fallback_avatar.webp', upload_to='avatars'),
        ),
    ]
