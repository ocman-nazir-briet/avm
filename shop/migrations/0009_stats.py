# Generated by Django 4.0.3 on 2022-07-15 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('month', models.CharField(max_length=20)),
                ('sale', models.IntegerField()),
            ],
        ),
    ]
