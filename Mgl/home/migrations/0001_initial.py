# Generated by Django 4.2.2 on 2023-06-13 03:37

from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=home.models.game_upload_handler)),
                ('user_score', models.FloatField(null=True)),
                ('metacritic_score', models.FloatField(null=True)),
                ('sumary', models.TextField(max_length=3000)),
                ('developers', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Plataform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True, max_length=1000, null=True)),
                ('score', models.FloatField()),
                ('release_date', models.DateTimeField(auto_now_add=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.game')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='plataform',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plataform', to='home.plataform'),
        ),
        migrations.AddField(
            model_name='game',
            name='plataforms',
            field=models.ManyToManyField(blank=True, related_name='plataforms', to='home.plataform'),
        ),
        migrations.AddField(
            model_name='game',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='home.tag'),
        ),
    ]
