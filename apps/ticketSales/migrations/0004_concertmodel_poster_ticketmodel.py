# Generated by Django 4.2.13 on 2024-05-21 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('ticketSales', '0003_timemodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='concertmodel',
            name='Poster',
            field=models.ImageField(default='noPhoto.jpg', upload_to='concertImages/'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ticketModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticketImage', models.ImageField(upload_to='TicketImages/')),
                ('Name', models.CharField(max_length=100)),
                ('Price', models.IntegerField()),
                ('ProfilrModel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.profilemodel')),
                ('timeModel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketSales.timemodel')),
            ],
        ),
    ]