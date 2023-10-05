# Generated by Django 4.2.5 on 2023-10-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewapp', '0004_alter_manager_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='FLtester',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('name', models.CharField(max_length=64, verbose_name='名称')),
                ('date', models.DateField(verbose_name='日期')),
                ('time', models.TimeField(verbose_name='时间')),
                ('Vot_50', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Vot_24', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Vot_5', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Vot_3', models.DecimalField(decimal_places=2, max_digits=4)),
                ('photo1', models.BooleanField()),
                ('photo2', models.BooleanField()),
                ('Laser_beam_on_off', models.BooleanField()),
                ('Vot_load1', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Vot_load2', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Vot_laser1', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Vot_laser2', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Triger_laser1', models.BooleanField()),
                ('Triger_laser2', models.BooleanField()),
                ('GPIO_0', models.BooleanField()),
                ('GPIO_1', models.BooleanField()),
                ('GPIO_2', models.BooleanField()),
                ('GPIO_3', models.BooleanField()),
            ],
        ),
        migrations.AlterModelTable(
            name='manager',
            table='reviewapp_manager',
        ),
    ]