# Generated by Django 3.2.7 on 2021-09-11 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_alter_student_thesis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='thesis',
            field=models.FileField(blank=True, null=True, upload_to='uploads'),
        ),
    ]