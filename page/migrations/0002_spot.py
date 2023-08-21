# Generated by Django 4.2.3 on 2023-07-26 00:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("page", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Spot",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=200)),
                ("latitude", models.DecimalField(decimal_places=6, max_digits=9)),
                ("longitude", models.DecimalField(decimal_places=6, max_digits=9)),
                ("website", models.URLField(blank=True, null=True)),
            ],
        ),
    ]
