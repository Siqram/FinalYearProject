# Generated by Django 3.0.6 on 2020-06-02 16:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qcareers', '0020_adminrequests'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AdminRequests',
            new_name='AdminRequest',
        ),
    ]
