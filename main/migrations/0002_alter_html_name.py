# Generated by Django 5.0.6 on 2024-06-19 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='html',
            name='name',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
