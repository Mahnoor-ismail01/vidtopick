# Generated by Django 3.2 on 2022-05-02 01:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srtgen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='srtgen',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='srt_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['srt'])]),
        ),
        migrations.AlterField(
            model_name='srtgen',
            name='preview',
            field=models.FileField(blank=True, null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])]),
        ),
    ]
