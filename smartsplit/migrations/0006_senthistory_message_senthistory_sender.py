# Generated by Django 4.2.3 on 2023-07-31 19:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("smartsplit", "0005_senthistory"),
    ]

    operations = [
        migrations.AddField(
            model_name="senthistory",
            name="message",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="senthistory",
            name="sender",
            field=models.CharField(default="", max_length=100),
        ),
    ]
