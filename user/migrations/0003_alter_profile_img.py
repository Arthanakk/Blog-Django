# Generated by Django 5.0.4 on 2024-07-30 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='default.png', upload_to='blog-pics'),
        ),
    ]
