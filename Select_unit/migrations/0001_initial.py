# Generated by Django 2.2.7 on 2019-12-05 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ac_name', models.CharField(max_length=255)),
                ('Ac_Location', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ChangeInAC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_temp', models.CharField(max_length=10)),
                ('current_fan', models.IntegerField()),
                ('Name_of_changeMaker', models.CharField(max_length=255)),
                ('AC_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Select_unit.AC')),
            ],
        ),
    ]
