# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-10 08:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0004_auto_20151229_1306'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_auto_20160107_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date_sent', models.DateTimeField()),
                ('date_received', models.DateTimeField()),
                ('mreceiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mreceiver', to=settings.AUTH_USER_MODEL)),
                ('msender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='USchoolProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=50)),
                ('school_ancronym', models.CharField(blank=True, max_length=15, null=True)),
                ('State', models.CharField(max_length=60)),
                ('Address', models.CharField(max_length=200)),
                ('faculty', models.CharField(blank=True, max_length=50, null=True)),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
                ('begin', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_scountry', to='cities_light.Country')),
            ],
        ),
        migrations.RemoveField(
            model_name='useraddress',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userdefaultaddress',
            name='billing',
        ),
        migrations.RemoveField(
            model_name='userdefaultaddress',
            name='shipping',
        ),
        migrations.RemoveField(
            model_name='userdefaultaddress',
            name='user',
        ),
        migrations.RemoveField(
            model_name='uprofile',
            name='department',
        ),
        migrations.RemoveField(
            model_name='uprofile',
            name='faculty',
        ),
        migrations.RemoveField(
            model_name='uprofile',
            name='school',
        ),
        migrations.AddField(
            model_name='uprofile',
            name='bio',
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='uprofile',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_country', to='cities_light.Country'),
        ),
        migrations.AddField(
            model_name='uprofile',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='UserAddress',
        ),
        migrations.DeleteModel(
            name='UserDefaultAddress',
        ),
    ]
