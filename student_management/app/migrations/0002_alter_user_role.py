# Generated by Django 4.1.2 on 2022-12-29 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('student', 'Student'), ('faculty', 'Faculty'), ('administrator', 'Administrator')], max_length=255),
        ),
    ]