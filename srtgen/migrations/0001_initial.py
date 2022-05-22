# Generated by Django 3.2 on 2022-05-02 01:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_remove_authuser_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Srtgen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('title', models.CharField(max_length=1000)),
                ('preview', models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])])),
                ('file', models.FileField(null=True, upload_to='srt_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['srt'])])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.authuser')),
            ],
        ),
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srtgen.srtgen')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.authuser')),
            ],
        ),
    ]