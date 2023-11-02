# Generated by Django 4.2.5 on 2023-11-02 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("engineer_utilization", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Status",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(default="-", max_length=50)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RemoveField(
            model_name="resource",
            name="position",
        ),
        migrations.AlterField(
            model_name="designation",
            name="name",
            field=models.CharField(default="-", max_length=100),
        ),
        migrations.AlterField(
            model_name="level",
            name="name",
            field=models.CharField(default="1", max_length=50),
        ),
        migrations.AlterField(
            model_name="projectresource",
            name="role",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="resource",
            name="gender",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name="Position",
        ),
        migrations.AddField(
            model_name="resource",
            name="status",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="engineer_utilization.status",
            ),
        ),
    ]
