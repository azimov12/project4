# Generated by Django 4.2.4 on 2023-09-01 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppAndroid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(default='', max_length=25)),
                ('app_size', models.SmallIntegerField(default=32)),
            ],
        ),
        migrations.CreateModel(
            name='AppIOS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(default='', max_length=25)),
                ('app_size', models.SmallIntegerField(default=32)),
            ],
        ),
    ]
