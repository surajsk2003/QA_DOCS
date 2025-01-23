# Generated by Django 5.1.5 on 2025-01-23 20:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Document",
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
                    "uploaded_file",
                    models.FileField(
                        upload_to="documents/", verbose_name="Uploaded File"
                    ),
                ),
                (
                    "uploaded_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Uploaded At"),
                ),
                (
                    "file_name",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="File Name"
                    ),
                ),
            ],
            options={
                "verbose_name": "Document",
                "verbose_name_plural": "Documents",
            },
        ),
        migrations.CreateModel(
            name="QuestionAnswer",
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
                ("question", models.CharField(max_length=512, verbose_name="Question")),
                ("answer", models.TextField(verbose_name="Answer")),
                (
                    "asked_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Asked At"),
                ),
                (
                    "document",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="qa_pairs",
                        to="questions.document",
                        verbose_name="Document",
                    ),
                ),
            ],
            options={
                "verbose_name": "Question Answer",
                "verbose_name_plural": "Question Answers",
            },
        ),
    ]
