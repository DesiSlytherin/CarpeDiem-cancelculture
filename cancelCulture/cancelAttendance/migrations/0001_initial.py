# Generated by Django 4.1.3 on 2023-03-17 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='leavereq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=256)),
                ('Register_Number', models.PositiveIntegerField()),
                ('Department', models.CharField(choices=[('CSE', 'CSE'), ('IT', 'IT'), ('MECH', 'MECH'), ('ECE', 'ECE'), ('EEE', 'EEE')], max_length=256)),
                ('Reason', models.CharField(choices=[('Casual', 'Casual'), ('Emergency', 'Emergency'), ('Medical', 'Medical'), ('Others', 'Others')], max_length=256)),
                ('Initial_Date', models.DateField()),
                ('Final_Date', models.DateField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='req_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
