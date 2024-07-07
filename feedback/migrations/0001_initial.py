# Generated by Django 5.0.4 on 2024-07-07 17:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField()),
                ('comment', models.TextField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor')),
            ],
        ),
    ]
