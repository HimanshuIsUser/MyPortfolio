# Generated by Django 4.0.5 on 2022-09-19 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_service_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(default='', upload_to='polls/images'),
        ),
    ]
