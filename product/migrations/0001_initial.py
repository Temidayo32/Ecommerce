# Generated by Django 4.1 on 2022-09-07 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
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
                ("name", models.CharField(max_length=50)),
                ("real", models.FloatField()),
                ("discount", models.FloatField(blank=True, null=True)),
                ("description", models.TextField()),
                ("bestseller", models.BooleanField(default=False)),
                ("featured", models.BooleanField(default=False)),
                ("new", models.BooleanField(default=False)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("S", "Supermarket"),
                            ("E", "Electronics"),
                            ("C", "Computer & Other Accessories"),
                            ("P", "Mobile Phone & Accessories"),
                        ],
                        max_length=1,
                    ),
                ),
                ("slug", models.SlugField(unique=True)),
                (
                    "ratings",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (1, "Very Poor"),
                            (2, "Poor"),
                            (3, "Good"),
                            (4, "Very Good"),
                            (5, "Excellent"),
                        ],
                        null=True,
                    ),
                ),
                ("reviews", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
