# Generated by Django 4.2.10 on 2024-02-28 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('enrollment', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=35)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('mobile', models.IntegerField(unique=True)),
                ('dob', models.DateField()),
                ('total_issues', models.IntegerField(default=0)),
                ('current_issues', models.IntegerField(default=0)),
                ('present', models.BooleanField(default=False)),
                ('intime', models.DateTimeField(null=True)),
                ('outtime', models.DateTimeField(null=True)),
                ('panenlty', models.IntegerField(default=0)),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
    ]
