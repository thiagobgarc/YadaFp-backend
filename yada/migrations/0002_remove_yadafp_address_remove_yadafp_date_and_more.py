# Generated by Django 4.2 on 2023-05-03 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yada', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yadafp',
            name='address',
        ),
        migrations.RemoveField(
            model_name='yadafp',
            name='date',
        ),
        migrations.RemoveField(
            model_name='yadafp',
            name='service',
        ),
        migrations.RemoveField(
            model_name='yadafp',
            name='signDate',
        ),
        migrations.RemoveField(
            model_name='yadafp',
            name='signName',
        ),
        migrations.RemoveField(
            model_name='yadafp',
            name='signPhone',
        ),
        migrations.RemoveField(
            model_name='yadafp',
            name='text',
        ),
    ]
