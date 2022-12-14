# Generated by Django 4.0.3 on 2022-07-02 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_agents'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('date', models.CharField(max_length=20)),
                ('picture', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='')),
                ('type', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]
