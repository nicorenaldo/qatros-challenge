# Generated by Django 3.1.1 on 2020-09-23 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='poster/')),
                ('code', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_depart', models.TimeField()),
                ('time_arrival', models.TimeField()),
                ('day', models.CharField(choices=[('SU', 'Sunday'), ('MO', 'Monday'), ('TH', 'Thursday'), ('WE', 'Wednesday'), ('TU', 'Tuesday'), ('FR', 'Friday'), ('SA', 'Saturday')], default='SU', max_length=2)),
                ('code', models.SlugField(blank=True, null=True, unique=True)),
                ('bus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sample2.bus')),
                ('destination', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='sample2.station')),
                ('origin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origin', to='sample2.station')),
            ],
        ),
    ]
