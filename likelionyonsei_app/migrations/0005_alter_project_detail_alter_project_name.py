# Generated by Django 4.0.4 on 2022-08-17 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likelionyonsei_app', '0004_rename_post_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='detail',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=10),
        ),
    ]
