# Generated by Django 3.2.3 on 2024-12-20 06:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190821_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Blog Description'),
        ),
    ]
