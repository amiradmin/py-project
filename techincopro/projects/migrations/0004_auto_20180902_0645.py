# Generated by Django 2.1 on 2018-09-02 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_subproject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subproject',
            name='consultant',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='subproject',
            name='mc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='subproject',
            name='owner',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='subproject',
            name='tpa',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
