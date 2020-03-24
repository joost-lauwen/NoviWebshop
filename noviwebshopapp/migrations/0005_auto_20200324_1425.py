# Generated by Django 2.2.6 on 2020-03-24 13:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('noviwebshopapp', '0004_auto_20200317_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=25)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='accesrecord',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 3, 24, 14, 25, 1, 119559)),
        ),
        migrations.AlterField(
            model_name='painting',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2020, 3, 24, 14, 25, 1, 118562)),
        ),
    ]
