# Generated by Django 4.2.5 on 2023-11-21 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('migass', '0003_remove_posts_short_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='full_desc',
            new_name='desc',
        ),
    ]
