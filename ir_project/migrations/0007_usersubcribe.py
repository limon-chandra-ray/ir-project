# Generated by Django 4.2.5 on 2023-10-06 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ir_project', '0006_usercontact_created_at_usercontact_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSubcribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
