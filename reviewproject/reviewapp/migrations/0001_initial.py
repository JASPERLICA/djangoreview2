# Generated by Django 4.2.5 on 2023-10-03 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID number')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('date', models.DateField(verbose_name='date')),
                ('time', models.TimeField(verbose_name='time')),
            ],
        ),
    ]