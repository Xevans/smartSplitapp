# Generated by Django 4.2.3 on 2023-07-31 13:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("smartsplit", "0003_rename_reqest_amount_requests_request_amount"),
    ]

    operations = [
        migrations.AddField(
            model_name="requests",
            name="recipient",
            field=models.CharField(default="", max_length=100),
        ),
    ]
