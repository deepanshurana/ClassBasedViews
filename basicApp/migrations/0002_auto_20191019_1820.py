# Generated by Django 2.2.5 on 2019-10-19 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='prinicipal',
            new_name='principal',
        ),
    ]