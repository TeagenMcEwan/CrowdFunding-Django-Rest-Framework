# Generated by Django 3.0.8 on 2020-08-19 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_pledge'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledge',
            name='supporter',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]