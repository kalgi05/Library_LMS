# Generated by Django 4.2.10 on 2024-03-04 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='category',
            field=models.CharField(choices=[('MG', 'Management'), ('DB', 'Database'), ('JN', 'Journal'), ('CS', 'Computer Science')], default='Select the Category', max_length=5),
        ),
    ]
