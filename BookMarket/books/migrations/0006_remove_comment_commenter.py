# Generated by Django 5.0.6 on 2024-07-02 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_remove_author_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='commenter',
        ),
    ]
