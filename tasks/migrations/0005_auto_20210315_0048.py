# Generated by Django 3.1.7 on 2021-03-14 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20210315_0046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-complete'], 'verbose_name': 'Task', 'verbose_name_plural': 'Task'},
        ),
    ]