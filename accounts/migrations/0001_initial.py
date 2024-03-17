# Generated by Django 5.0.3 on 2024-03-17 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone_number', models.CharField(max_length=11, unique=True, verbose_name='شماره تلفن ')),
                ('email', models.EmailField(max_length=250, unique=True, verbose_name='ایمیل ')),
                ('full_name', models.CharField(max_length=100, verbose_name='نام ')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='media/avatars/Y%M%D')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]