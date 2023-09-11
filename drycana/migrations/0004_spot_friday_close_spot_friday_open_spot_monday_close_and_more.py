# Generated by Django 4.2.3 on 2023-09-11 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("drycana", "0003_remove_spot_affiliate_apps_spotaffiliate"),
    ]

    operations = [
        migrations.AddField(
            model_name="spot",
            name="friday_close",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="spot",
            name="friday_open",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="spot",
            name="monday_close",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="spot",
            name="monday_open",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="spot",
            name="saturday_close",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="spot",
            name="saturday_open",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="spot",
            name="sunday_close",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="spot",
            name="sunday_open",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="spot",
            name="thursday_close",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="spot",
            name="thursday_open",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="spot",
            name="tuesday_close",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="spot",
            name="tuesday_open",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="spot",
            name="wednesday_close",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="spot",
            name="wednesday_open",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="MenuItem",
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
                ("item_name", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                (
                    "spot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="drycana.spot"
                    ),
                ),
            ],
        ),
    ]