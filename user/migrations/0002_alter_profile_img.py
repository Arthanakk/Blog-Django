# Generated by Django 5.0.4 on 2024-07-30 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='reviewpic02.jpeg', upload_to='blog-pics'),
        ),
    ]