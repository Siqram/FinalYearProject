# Generated by Django 3.0.6 on 2020-06-01 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qcareers', '0006_module_module_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='skill_slug',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
