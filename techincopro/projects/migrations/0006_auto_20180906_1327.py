# Generated by Django 2.1 on 2018-09-06 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20180902_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subproject',
            name='contractor',
            field=models.CharField(max_length=255),
        ),
    ]
