# Generated by Django 5.0 on 2023-12-28 13:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('adress', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('body', models.CharField(max_length=100)),
                ('postId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.post')),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
    ]
