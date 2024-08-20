# Generated by Django 5.0.6 on 2024-08-20 11:34

import main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_css_name_alter_html_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='name',
            field=models.SlugField(max_length=120, unique=True, validators=[main.models.folder_name_validator]),
        ),
    ]
