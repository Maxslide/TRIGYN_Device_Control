# Generated by Django 2.2.7 on 2019-12-06 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Select_unit', '0004_changeingeyser_geyser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bulb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bulb_name', models.CharField(max_length=255)),
                ('Bulb_Latitude', models.CharField(max_length=255)),
                ('Bulb_Longitude', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ChangeInBulb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_state', models.IntegerField()),
                ('Brightness', models.IntegerField()),
                ('Color', models.CharField(max_length=20)),
                ('Effect', models.IntegerField()),
                ('Name_of_changeMaker', models.CharField(max_length=255)),
                ('Bulb_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Select_unit.Geyser')),
            ],
        ),
    ]
