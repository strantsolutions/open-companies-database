# Generated by Django 4.2.13 on 2024-05-21 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("companies", "0002_alter_company_categories_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CompanyCrustdataCompanyAssociation",
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
                ("crustdata_company_id", models.CharField(max_length=256, unique=True)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="companies.company",
                        unique=True,
                    ),
                ),
            ],
        ),
    ]
