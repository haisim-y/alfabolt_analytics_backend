# Generated by Django 4.2.5 on 2023-09-27 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineer_utilization', '0003_alter_resource_designation_alter_resource_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectresource',
            name='role',
            field=models.CharField(choices=[('Frontend', 'Frontend Developer'), ('Backend', 'Backend Developer'), ('Devops', 'Devops Developer'), ('Cloud', 'CLoud Architect'), ('Data Science', 'Data Scientist')], max_length=100),
        ),
    ]