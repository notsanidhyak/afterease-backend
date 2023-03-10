# Generated by Django 4.1.7 on 2023-03-10 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AadhaarCard",
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
                ("aadhaar_number", models.CharField(max_length=12, unique=True)),
                ("full_name", models.CharField(max_length=100)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                        max_length=1,
                    ),
                ),
                ("date_of_birth", models.DateField()),
                ("address_line", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=50)),
                ("pincode", models.CharField(max_length=6)),
                ("phone_number", models.CharField(max_length=10)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="DeathCertificate",
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
                ("date_of_death", models.DateField()),
                ("place_of_death", models.CharField(max_length=100)),
                ("cause_of_death", models.CharField(max_length=100)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                        max_length=1,
                    ),
                ),
                ("age", models.IntegerField()),
                ("father_name", models.CharField(max_length=100)),
                ("mother_name", models.CharField(max_length=100)),
                ("informant_relationship", models.CharField(max_length=100)),
                ("informant_adhaar", models.CharField(max_length=12, null=True)),
                ("registration_date", models.DateTimeField(auto_now_add=True)),
                ("registration_place", models.CharField(max_length=100)),
                ("registration_number", models.CharField(max_length=20)),
                (
                    "aadhaar_number",
                    models.CharField(max_length=12, null=True, unique=True),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("Pending", "Pending"), ("Approved", "Approved")],
                        default="Pending",
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DrivingLicense",
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
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("date_of_birth", models.DateField()),
                ("address", models.CharField(max_length=255)),
                ("license_number", models.CharField(max_length=255, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("date_expires", models.DateField()),
                ("adhaar_number", models.CharField(max_length=12, null=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Informant",
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
                ("phone_number", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="PANCard",
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
                ("pan_number", models.CharField(max_length=10, unique=True)),
                ("holder_name", models.CharField(max_length=50)),
                ("father_name", models.CharField(max_length=50)),
                ("date_of_birth", models.DateField()),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                        max_length=1,
                    ),
                ),
                ("address", models.CharField(max_length=100)),
                (
                    "aadhaar_number",
                    models.CharField(max_length=12, null=True, unique=True),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Pensioner",
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
                ("PPO", models.IntegerField(unique=True)),
                ("pensioner_name", models.CharField(max_length=50)),
                ("pensioner_address", models.CharField(max_length=100)),
                ("pension_amount", models.FloatField()),
                ("bank_name", models.CharField(max_length=50)),
                ("bank_account_number", models.CharField(max_length=20)),
                (
                    "bank_account_type",
                    models.CharField(
                        choices=[("Savings", "Savings"), ("Current", "Current")],
                        max_length=10,
                    ),
                ),
                ("ifsc_code", models.CharField(max_length=15)),
                (
                    "pension_status",
                    models.CharField(
                        choices=[("Active", "Active"), ("Stopped", "Stopped")],
                        default="Active",
                        max_length=15,
                    ),
                ),
                ("adhaar_number", models.CharField(max_length=12, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="VoterID",
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
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("date_of_birth", models.DateField()),
                ("address", models.CharField(max_length=255)),
                ("voter_id_number", models.CharField(max_length=255, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("adhaar_number", models.CharField(max_length=12, null=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="InformantDeathCertificate",
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
                    "death_certificate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="integrations.deathcertificate",
                    ),
                ),
                (
                    "informant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="integrations.informant",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="informant",
            name="death_certificates",
            field=models.ManyToManyField(
                through="integrations.InformantDeathCertificate",
                to="integrations.deathcertificate",
            ),
        ),
    ]
