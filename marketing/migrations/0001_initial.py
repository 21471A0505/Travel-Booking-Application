# Generated by Django 2.2.4 on 2019-08-23 16:22

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
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_title', models.CharField(max_length=100, verbose_name='Group Title')),
                ('group_description', models.TextField(blank=True, null=True, verbose_name='Group Descritpion')),
                ('group_added_at', models.DateTimeField(auto_now_add=True, verbose_name='Added Date')),
                ('group_updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('group_created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscriber_email', models.EmailField(max_length=100, verbose_name='Email Address')),
                ('subscriber_first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='First Name')),
                ('subscriber_last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Last Name')),
                ('subscriber_contact', models.CharField(blank=True, max_length=100, null=True, verbose_name='Contact Number')),
                ('subscriber_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='marketing.Group', verbose_name='Group')),
            ],
        ),
    ]
