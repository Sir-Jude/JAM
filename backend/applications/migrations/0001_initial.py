# Generated by Django 4.2.5 on 2023-10-12 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("dependencies", "0001_initial"),
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Application",
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
                ("position", models.CharField(max_length=255)),
                ("company", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("cover_letter_text", models.TextField(blank=True)),
                (
                    "cover_letter_file",
                    models.FileField(
                        blank=True, upload_to="saved_files/cover_letters/"
                    ),
                ),
                ("cv_short_description", models.CharField(blank=True, max_length=400)),
                ("cv_file", models.FileField(blank=True, upload_to="saved_files/cvs/")),
                ("company_email", models.EmailField(max_length=255)),
                ("company_address", models.CharField(blank=True, max_length=255)),
                ("source", models.CharField(blank=True, max_length=255)),
                (
                    "recruiter_name",
                    models.CharField(default="John Doe", max_length=255),
                ),
                ("recruiter_position", models.CharField(default="CEO", max_length=255)),
                ("status_date", models.DateTimeField(auto_now_add=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "application_language",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="dependencies.language",
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="profiles.profile",
                    ),
                ),
                (
                    "recruiter_gender",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="dependencies.gender",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="dependencies.status",
                    ),
                ),
            ],
        ),
    ]
