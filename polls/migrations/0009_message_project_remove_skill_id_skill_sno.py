# Generated by Django 4.0.5 on 2022-09-25 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_skill_remove_service_skill_remove_service_width'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=111)),
                ('subject', models.CharField(max_length=500)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('pic', models.ImageField(default='', upload_to='polls/images')),
                ('name', models.CharField(max_length=111)),
                ('domain', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='skill',
            name='id',
        ),
        migrations.AddField(
            model_name='skill',
            name='sno',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
