# Generated by Django 2.2.7 on 2019-12-09 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Select_unit', '0007_changeinwifi_smart_wifi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car_Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Booking_Name', models.CharField(max_length=255)),
                ('Booked_Value', models.IntegerField()),
                ('Booked_Code', models.CharField(max_length=10)),
            ],
        ),
    ]
