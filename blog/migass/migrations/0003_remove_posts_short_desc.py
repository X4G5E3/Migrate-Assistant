# Generated by Django 4.2.5 on 2023-11-16 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('migass', '0002_alter_posts_create_date_alter_posts_img_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='short_desc',
        ),
    ]