# Generated by Django 4.2.3 on 2023-08-25 09:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("username", models.CharField(blank=True, max_length=200, null=True)),
                ("email", models.EmailField(blank=True, max_length=100, null=True)),
                ("Issue", models.TextField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Recipes",
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
                ("Recipe_name", models.CharField(max_length=100, null=True)),
                (
                    "Recipe_Type",
                    models.CharField(
                        choices=[
                            ("North Indian", "North Indian"),
                            ("South Indian", "South Indian"),
                            ("Italian", "Italian"),
                            ("Healthy Salad", "Healthy Salad"),
                            ("Bakery", "Bakery"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                ("Recipe_Owner", models.CharField(max_length=100, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "Image",
                    models.ImageField(
                        blank=True, null=True, upload_to="accounts/Food_pics/images/"
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, max_length=2000, null=True),
                ),
                (
                    "ingredients",
                    models.TextField(blank=True, max_length=1000, null=True),
                ),
                ("servings", models.CharField(blank=True, max_length=5, null=True)),
                ("time", models.CharField(blank=True, max_length=5, null=True)),
                ("calories", models.CharField(blank=True, max_length=5, null=True)),
                ("Steps", models.TextField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserName_Profile",
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
                    "Email_Id",
                    models.EmailField(
                        blank=True, max_length=100, null=True, unique=True
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                ("phone", models.CharField(blank=True, max_length=200, null=True)),
                ("password", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "Image",
                    models.ImageField(
                        blank=True,
                        default="accounts/profile_pics/images/profile1.png",
                        null=True,
                        upload_to="accounts/profile_pics/images/",
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="review",
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
                ("content", models.TextField()),
                ("username", models.CharField(max_length=80, null=True)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "rating",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
                ),
                (
                    "recipes2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="accounts.recipes",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="recipes",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="food",
                to="accounts.username_profile",
            ),
        ),
    ]
