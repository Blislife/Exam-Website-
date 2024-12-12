# Generated by Django 5.1.2 on 2024-10-29 20:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=80)),
                ('lastName', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=80)),
            ],
        ),
        migrations.DeleteModel(
            name='studentNames',
        ),
        migrations.AddField(
            model_name='item',
            name='studentUsers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.students'),
        ),
    ]
