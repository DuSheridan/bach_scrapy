# Generated by Django 3.2.4 on 2021-07-24 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='name',
        ),
        migrations.AddField(
            model_name='test',
            name='text',
            field=models.TextField(default='old'),
            preserve_default=False,
        ),
    ]
