# Generated by Django 4.2.3 on 2023-09-11 05:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("page", "0005_spot_friday_close_spot_friday_open_spot_monday_close_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="spot",
            name="friday_close",
        ),
        migrations.RemoveField(
            model_name="spot",
            name="friday_open",
        ),
        migrations.RemoveField(
            model_name="spot",
            name="monday_close",
        ),
        migrations.RemoveField(
            model_name="spot",
            name="monday_open",
        ),
        migrations.RemoveField(
            model_name="spot",
            name="saturday_close",
        ),
        migrations.RemoveField(
            model_name="spot",
            name="saturday_open",
        ),
        migrations.RemoveField(
            model_name="spot",
            name="sunday_close",
        ),
        migrations.RemoveField(
            model_name="spot",
            name="sunday_open",
        ),
        migrations.RemoveField(
            model_name="spot",
            name="thursday_close",
        ),
        migrations.RemoveField(
            model_name="spot",
            name="thursday_open",
        ),
        migrations.RemoveField(
            model_name="spot",
            name="tuesday_close",
        ),
        migrations.RemoveField(
            model_name="spot",
            name="tuesday_open",
        ),
        migrations.RemoveField(
            model_name="spot",
            name="wednesday_close",
        ),
        migrations.RemoveField(
            model_name="spot",
            name="wednesday_open",
        ),
        migrations.DeleteModel(
            name="MenuItem",
        ),
    ]
