# Generated by Django 3.2.7 on 2021-09-12 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_alter_teacher_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messagemodel',
            name='image',
        ),
        migrations.RemoveField(
            model_name='student',
            name='thesis',
        ),
        migrations.AddField(
            model_name='messagemodel',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads'),
        ),
    ]
