# Generated by Django 5.1.1 on 2024-09-20 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='role',
            field=models.CharField(choices=[('mentor', 'Mentor'), ('admin', 'Admin')], default='mentor', max_length=10),
        ),
    ]
