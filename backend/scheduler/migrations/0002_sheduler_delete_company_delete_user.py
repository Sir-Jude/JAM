# Generated by Django 4.2.5 on 2023-09-27 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "applications",
            "0002_rename_application_language_id_application_application_language_and_more",
        ),
        ("users", "0003_alter_user_birthday_alter_user_portfolio_link_and_more"),
        ("scheduler", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sheduler",
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
                ("date", models.DateTimeField()),
                (
                    "application",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="applications.application",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.user"
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Company",
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]
