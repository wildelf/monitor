# Generated by Django 2.0.2 on 2018-05-03 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_processdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='ip',
        ),
    ]
