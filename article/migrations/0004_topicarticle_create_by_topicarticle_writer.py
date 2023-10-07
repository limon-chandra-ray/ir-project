# Generated by Django 4.2.5 on 2023-10-03 22:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0003_alter_topicarticle_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='topicarticle',
            name='create_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='topicarticle',
            name='writer',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
