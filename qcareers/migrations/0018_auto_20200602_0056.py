# Generated by Django 3.0.6 on 2020-06-01 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qcareers', '0017_recommendation_currentdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recommendation',
            old_name='currentdate',
            new_name='dateAndTimeOfRec',
        ),
    ]