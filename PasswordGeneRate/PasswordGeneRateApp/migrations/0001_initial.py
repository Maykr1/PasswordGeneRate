# Generated by Django 5.1.1 on 2024-10-15 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insult', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]