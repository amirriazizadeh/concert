# Generated by Django 4.2.13 on 2024-05-21 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketSales', '0002_alter_locationmodel_address_timemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='timemodel',
            name='Status',
            field=models.IntegerField(choices=[(1, 'فروش بلیط آغاز شده است'), (2, 'پایان'), (4, 'در حال فروش...'), (3, 'کنسل شده')], default=1),
        ),
    ]