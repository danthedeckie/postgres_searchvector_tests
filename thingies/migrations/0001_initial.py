# Generated by Django 5.1.5 on 2025-01-27 20:14

import django.contrib.postgres.search
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('search_vector', django.contrib.postgres.search.SearchVectorField()),
            ],
        ),
    ]
