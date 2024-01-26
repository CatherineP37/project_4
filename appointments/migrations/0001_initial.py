# Generated by Django 4.2.9 on 2024-01-26 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id_number', models.IntegerField()),
                ('first_name', models.CharField()),
                ('last_name', models.CharField()),
                ('email_address', models.EmailField(max_length=254)),
                ('postal_address', models.CharField()),
                ('phone_number', models.IntegerField()),
            ],
        ),
    ]
