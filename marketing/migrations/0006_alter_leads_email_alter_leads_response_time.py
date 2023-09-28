# Generated by Django 4.2.5 on 2023-09-27 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0005_alter_leads_lead_status_alter_leads_sector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='leads',
            name='response_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
