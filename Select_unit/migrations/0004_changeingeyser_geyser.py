# Generated by Django 2.2.7 on 2019-12-06 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Select_unit', '0003_changeinfan_fan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Geyser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Geyser_name', models.CharField(max_length=255)),
                ('Geyser_Latitude', models.CharField(max_length=255)),
                ('Geyser_Longitude', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ChangeInGeyser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_state', models.IntegerField()),
                ('schedule_on_time', models.CharField(max_length=255)),
                ('schedule_off_time', models.CharField(max_length=255)),
                ('follow_schedule_for_week', models.IntegerField()),
                ('Name_of_changeMaker', models.CharField(max_length=255)),
                ('Geyser_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Select_unit.Geyser')),
            ],
        ),
    ]