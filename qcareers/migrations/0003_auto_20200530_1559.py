# Generated by Django 3.0.4 on 2020-05-30 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qcareers', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_role', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_name', models.CharField(max_length=250, null=True)),
                ('job', models.ManyToManyField(to='qcareers.Job')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AddField(
            model_name='module',
            name='skills',
            field=models.ManyToManyField(to='qcareers.Skill'),
        ),
    ]
