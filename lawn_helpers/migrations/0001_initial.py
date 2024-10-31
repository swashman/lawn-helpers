# Generated by Django 4.2.11 on 2024-10-31 01:45

# Django
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="General",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "permissions": (
                    ("basic_access", "Basic access to this app"),
                    ("it_commands", "Can use IT commands"),
                ),
                "managed": False,
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="Link",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField(max_length=500)),
                ("name", models.CharField(max_length=255, unique=True)),
                ("url", models.CharField(max_length=255)),
                ("thumbnail", models.CharField(max_length=255)),
            ],
            options={
                "permissions": (("manage_links", "Can manage links"),),
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="GroupWelcome",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.TextField()),
                ("enabled", models.BooleanField(default=True)),
                ("channel", models.BigIntegerField()),
                (
                    "group",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="auth.group"
                    ),
                ),
            ],
            options={
                "verbose_name": "Group Welcome Message",
                "verbose_name_plural": "Group Welcome Messages",
            },
        ),
    ]
