# Generated by Django 5.0.6 on 2024-05-28 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poem',
            old_name='author_id',
            new_name='author',
        ),
    ]
