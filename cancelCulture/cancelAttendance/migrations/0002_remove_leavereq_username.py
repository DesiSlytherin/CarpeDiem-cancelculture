# Generated by Django 4.1.3 on 2023-03-17 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cancelAttendance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leavereq',
            name='username',
        ),
    ]
