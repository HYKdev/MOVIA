# Generated by Django 3.2.12 on 2022-05-26 17:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('main_image', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('main_image', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.TextField()),
                ('pubdate', models.CharField(max_length=10)),
                ('userating', models.IntegerField()),
                ('overview', models.TextField()),
                ('trailer', models.TextField()),
                ('actors', models.ManyToManyField(related_name='movies', to='movies.Actor')),
                ('directors', models.ManyToManyField(related_name='movies', to='movies.Director')),
                ('genres', models.ManyToManyField(to='movies.Genre')),
                ('like_users', models.ManyToManyField(related_name='like_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='actor',
            name='images',
            field=models.ManyToManyField(related_name='actors', to='movies.Image'),
        ),
        migrations.AddField(
            model_name='actor',
            name='like_users',
            field=models.ManyToManyField(related_name='like_actors', to=settings.AUTH_USER_MODEL),
        ),
    ]
