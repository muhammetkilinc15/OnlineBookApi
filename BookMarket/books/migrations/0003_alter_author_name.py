# Generated by Django 5.0.6 on 2024-06-28 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_author_alter_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=55),
        ),
    ]