# Generated by Django 4.2.3 on 2023-07-31 12:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("smartsplit", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="requests",
            old_name="req_amnt",
            new_name="reqest_amount",
        ),
        migrations.RemoveField(
            model_name="requests",
            name="profile",
        ),
        migrations.AddField(
            model_name="requests",
            name="sender",
            field=models.CharField(default="", max_length=100),
        ),
    ]
