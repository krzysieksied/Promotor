# Generated by Django 3.2.7 on 2021-09-11 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_alter_teacher_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Teacher', serialize=False, to='webapp.profiluser'),
        ),
    ]
