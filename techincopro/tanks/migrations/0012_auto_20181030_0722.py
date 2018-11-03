# Generated by Django 2.0.8 on 2018-10-30 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tanks', '0011_auto_20181030_0702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rt',
            old_name='Req_RT_Segment1',
            new_name='Req_2ND_Segment_From2',
        ),
        migrations.RenameField(
            model_name='rt',
            old_name='Req_RT_Segment2',
            new_name='Req_2ND_Segment_To2',
        ),
        migrations.AddField(
            model_name='rt',
            name='Req_3RD_Segment_From2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rt',
            name='Req_3RD_Segment_To2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rt',
            name='Req_4TH_Segment_From2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rt',
            name='Req_4TH_Segment_To2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rt',
            name='Req_5TH_Segment_From2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rt',
            name='Req_5TH_Segment_To2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rt',
            name='Req_RT_Segment_From1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rt',
            name='Req_RT_Segment_To1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
