# Generated by Django 3.0.5 on 2020-11-16 03:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middlename', models.CharField(blank=True, default='', max_length=50)),
                ('date_of_birth', models.DateField()),
                ('twitter_handle', models.CharField(max_length=20)),
                ('fb_handle', models.CharField(max_length=20)),
                ('insta_handle', models.CharField(max_length=20)),
                ('telephone', models.CharField(max_length=13)),
                ('website', models.CharField(blank=True, default='', max_length=50)),
                ('address1', models.TextField()),
                ('address2', models.TextField()),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zipcode', models.IntegerField(blank=True, null=True)),
                ('about', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'profiles',
            },
        ),
    ]
