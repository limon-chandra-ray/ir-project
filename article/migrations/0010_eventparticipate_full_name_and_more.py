# Generated by Django 4.2.5 on 2023-10-07 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_department_studentsession_eventparticipate'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventparticipate',
            name='full_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='eventparticipate',
            name='student_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
