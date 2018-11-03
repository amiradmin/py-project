# Generated by Django 2.0.8 on 2018-10-30 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tanks', '0010_auto_20181030_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='general',
            name='Joint_Course',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='Joint_Degree',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='Joint_No',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='Levelness_After_Weld_Date',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='Levelness_After_Weld_Deviation',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='Levelness_After_Weld_No',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='Levelness_After_Weld_Value',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='Levelness_Before_Weld_Date',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='Levelness_Before_Weld_Deviation',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='Levelness_Before_Weld_No',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='Levelness_Before_Weld_Value',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='Plumbness_After_Weld_Date',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='Plumbness_After_Weld_Deviation',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='Plumbness_After_Weld_No',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='Plumbness_After_Weld_Value',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='Plumbness_Before_Weld_Date',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='Plumbness_Before_Weld_Deviation',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='Plumbness_Before_Weld_No',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='Plumbness_Before_Weld_Value',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='Roundness_After_Weld_Date',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='Roundness_After_Weld_Deviation',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='Roundness_After_Weld_No',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='Roundness_After_Weld_Value',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='Roundness_Before_Weld_Deviation',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='Roundness_Before_Weld_No',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='general',
            name='Roundness_Before_Weld_Value',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Bevelling_Date',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Bevelling_No',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Cutting_Date',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Cutting_No',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Head_No',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='MT_Date',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='MT_No',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='MT_Result',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Material',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='PMINo',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='PMI_Date',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='PMI_Result',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Painting_Blasting_Date',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Painting_Blasting_No',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Painting_Blasting_Surface_Aria',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Painting_Blasting_Type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Painting_Final_Coat_Surface_Date',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Painting_Final_Coat_Surface_No',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Painting_Final_Coat_Surface_Thickness',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Painting_Primer_Coat_Surface_Date',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Painting_Primer_Coat_Surface_No',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Painting_Primer_Coat_Surface_Thickness',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Painting_Second_Coat_Surface_Date',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Painting_Second_Coat_Surface_No',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Painting_Second_Coat_Surface_Thickness',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Painting_Third_Coat_Surface_Date',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Painting_Third_Coat_Surface_No',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Painting_Third_Coat_Surface_Thickness',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Piece_Code1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Piece_Code2',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Piece_Name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Piece_No1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Piece_No2',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Thickness',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='generalpart',
            name='Weight',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
