# Generated by Django 4.2.5 on 2023-09-26 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("applications", "0001_initial"),
        ("users", "0001_initial"),
        ("dependencies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Simulation",
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
                (
                    "recruiter_attitude",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                ("json_file", models.TextField(blank=True, null=True)),
                ("review", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField()),
                (
                    "application_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="applications.application",
                    ),
                ),
                (
                    "language_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dependencies.language",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.user"
                    ),
                ),
            ],
        ),
    ]
