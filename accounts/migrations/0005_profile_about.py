# Generated by Django 4.2 on 2023-04-15 13:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_rename_username_profile_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="About",
            field=models.CharField(
                default=django.utils.timezone.now, help_text="About", max_length=200
            ),
            preserve_default=False,
        ),
    ]
