# Generated by Django 4.0.5 on 2022-09-19 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_alter_service_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=111)),
                ('width', models.CharField(max_length=111)),
            ],
        ),
    ]