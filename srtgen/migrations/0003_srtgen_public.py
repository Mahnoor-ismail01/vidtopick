# Generated by Django 3.2 on 2022-05-02 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srtgen', '0002_auto_20220502_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='srtgen',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
