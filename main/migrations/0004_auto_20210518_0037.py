# Generated by Django 3.2.3 on 2021-05-17 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_news'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.RenameField(
            model_name='news',
            old_name='cat',
            new_name='category',
        ),
    ]