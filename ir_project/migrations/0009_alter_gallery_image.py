# Generated by Django 4.2.5 on 2023-10-07 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ir_project', '0008_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='gallery/'),
        ),
    ]
