# Generated by Django 4.2.13 on 2024-05-21 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='concertModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('SingerName', models.CharField(max_length=100)),
                ('lenght', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='locationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=500)),
                ('Phone', models.CharField(max_length=11)),
                ('capacity', models.IntegerField()),
            ],
        ),
    ]
