# Generated by Django 5.0.6 on 2024-09-15 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('level', models.CharField(choices=[('admin', 'Administrator'), ('editor', 'Editor'), ('user', 'User')], default='user', max_length=10)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
