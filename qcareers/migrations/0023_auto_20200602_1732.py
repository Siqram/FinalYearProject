# Generated by Django 3.0.6 on 2020-06-02 16:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qcareers', '0022_auto_20200602_1731'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AdminRequesttt',
            new_name='AdminRequest',
        ),
    ]