# Generated by Django 4.0.5 on 2022-09-25 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_delete_skill_service_skill_service_width'),
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
        migrations.RemoveField(
            model_name='service',
            name='skill',
        ),
        migrations.RemoveField(
            model_name='service',
            name='width',
        ),
    ]
