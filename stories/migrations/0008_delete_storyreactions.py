# Generated by Django 4.2 on 2023-04-15 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0007_alter_storyreactions_story'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StoryReactions',
        ),
    ]
