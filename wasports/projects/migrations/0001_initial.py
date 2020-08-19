# Generated by Django 3.0.8 on 2020-08-19 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('goal', models.IntegerField()),
                ('image', models.URLField()),
                ('is_open', models.BooleanField()),
                ('date_created', models.DateTimeField()),
                ('owner', models.CharField(max_length=200)),
            ],
        ),
    ]
