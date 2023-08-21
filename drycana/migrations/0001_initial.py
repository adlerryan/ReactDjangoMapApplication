# Generated by Django 4.2.3 on 2023-07-31 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AffiliateApp",
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
                ("website", models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="LocationType",
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
                ("website", models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="MyModel",
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
                ("description", models.TextField()),
            ],
        ),
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
                (
                    "rating",
                    models.DecimalField(decimal_places=1, default=0.0, max_digits=3),
                ),
                ("cover_charge", models.BooleanField(default=False)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "affiliate_apps",
                    models.ManyToManyField(blank=True, to="drycana.affiliateapp"),
                ),
                (
                    "location_types",
                    models.ManyToManyField(blank=True, to="drycana.locationtype"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("website", models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="SpotImage",
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
                ("image", models.ImageField(upload_to="spot_images/")),
                ("is_main_image", models.BooleanField(default=False)),
                (
                    "spot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="additional_images",
                        to="drycana.spot",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="spot",
            name="tags",
            field=models.ManyToManyField(blank=True, to="drycana.tag"),
        ),
    ]
