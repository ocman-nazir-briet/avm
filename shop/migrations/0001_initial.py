# Generated by Django 4.0.3 on 2022-06-26 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='plots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('bath', models.IntegerField()),
                ('bed', models.IntegerField()),
                ('area', models.IntegerField(max_length=50)),
                ('date', models.CharField(max_length=20)),
                ('picture', models.ImageField(upload_to='')),
            ],
        ),
    ]
