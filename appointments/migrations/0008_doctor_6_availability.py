# Generated by Django 4.2.9 on 2024-01-26 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0007_doctor_5_availability'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_6_availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_id', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
