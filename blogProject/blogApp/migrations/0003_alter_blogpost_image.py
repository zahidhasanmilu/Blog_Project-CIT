# Generated by Django 4.1.7 on 2023-03-15 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_alter_blogpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default='default/default.png', upload_to='Blog Image/'),
        ),
    ]