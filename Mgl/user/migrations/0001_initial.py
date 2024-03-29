# Generated by Django 4.2.2 on 2023-06-13 03:37

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.TextField(max_length=20)),
                ('avatar', models.FileField(blank=True, null=True, upload_to=user.models.profile_upload_handler)),
                ('register_date', models.DateTimeField(auto_now=True, verbose_name=django.contrib.auth.models.User)),
                ('birth_date', models.DateField(null=True)),
                ('follow', models.ManyToManyField(blank=True, related_name='followed_by', to='user.profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile')),
            ],
        ),
    ]
