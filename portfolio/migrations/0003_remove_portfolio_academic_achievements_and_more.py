# Generated by Django 5.0.6 on 2024-06-14 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_portfolio_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='academic_achievements',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='projects',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='work_experience',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='about_me',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='conferences',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='course_work',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='extracurricular_activities',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='full_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='practices',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='skills',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
