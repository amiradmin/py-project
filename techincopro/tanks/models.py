from django.db import models
from projects.models import Project,SubProject
from django import forms
import os

# Create your models here.

class Tank(models.Model):
    tank_no = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    inner_material = models.CharField(max_length=255)
    outer_material = models.CharField(max_length=255)
    inner_diameter = models.FloatField()
    outer_diameter = models.FloatField()
    inner_hight = models.FloatField()
    outer_hight = models.FloatField()
    inner_no_of_course = models.CharField(max_length=255)
    outer_no_of_course = models.CharField(max_length=255)
    inner_roof_type = models.CharField(max_length=255)
    outer_roof_type = models.CharField(max_length=255)
    inner_roof_shape = models.CharField(max_length=255)
    outer_roof_shape = models.CharField(max_length=255)
    subcontractor = models.CharField(max_length=255)
    contractor = models.CharField(max_length=255)
    consultant = models.CharField(max_length=255)
    tpa = models.CharField(max_length=255)
    mc = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    first_image = models.ImageField(upload_to='tanks', blank=True)
    second_image = models.ImageField(upload_to='tanks', blank=True)
    third_image = models.ImageField(upload_to='tanks', blank=True)
    doc_rev_1 = models.FileField(upload_to='doct',null=True,blank=True)
    doc_rev_2 = models.FileField(upload_to='doct',null=True,blank=True)
    doc_rev_3 = models.FileField(upload_to='doct',null=True,blank=True)
    doc_rev_4 = models.FileField(upload_to='doct',null=True,blank=True)
    doc_rev_5 = models.FileField(upload_to='doct',null=True,blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    subproject = models.ForeignKey(SubProject, related_name="subproject_tank",null=True, blank=False,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.tank_no


class GeneralWelding(models.Model):
    row = models.IntegerField()
    tank_FK = models.ForeignKey(Tank, related_name="G1_tanks",null=True, blank=False,on_delete=models.DO_NOTHING)
    tank =models.CharField(max_length=255,null=True)
    location_1 =models.CharField(max_length=255,null=True)
    location_2 =models.CharField(max_length=255,null=True)
    joint_code_1 = models.CharField(max_length=255,null=True)
    joint_no_1 = models.CharField(max_length=255,null=True)
    joint_code_2 = models.CharField(max_length=255,null=True)
    joint_no_2 = models.CharField(max_length=255,null=True)
    thickness_1 = models.CharField(max_length=255,null=True)
    thickness_2= models.CharField(max_length=255,null=True)
    joint_lenght= models.CharField(max_length=255,null=True)
    joint_type= models.CharField(max_length=255,null=True)
    material_1= models.CharField(max_length=255,null=True)
    material_2= models.CharField(max_length=255,null=True)
    wps_no= models.CharField(max_length=255,null=True)
    fitup_date= models.DateField()
    fitup_no = models.CharField(max_length=255,null=True)
    welding_date = models.CharField(max_length=255,null=True)
    welding_no = models.CharField(max_length=255,null=True)
    welder_1 = models.CharField(max_length=255,null=True)
    welder_2 = models.CharField(max_length=255,null=True)
    welder_3 = models.CharField(max_length=255,null=True)
    welder_4 = models.CharField(max_length=255,null=True)
    VBT_REQ_date = models.CharField(max_length=255,null=True)
    VBT_REQ_no = models.CharField(max_length=255,null=True)
    VBT_REP_date = models.CharField(max_length=255,null=True)
    VBT_REP_No = models.CharField(max_length=255,null=True)

    OilTest_REQ_Date = models.CharField(max_length=255,null=True)
    OilTest_REQ_No = models.CharField(max_length=255,null=True)
    OilTest_REP_Date = models.CharField(max_length=255,null=True)
    OilTest_REP_No = models.CharField(max_length=255,null=True)

    HNT_REQ_Date = models.CharField(max_length=255,null=True)
    HNT_REQ_No = models.CharField(max_length=255,null=True)
    HT_Value = models.CharField(max_length=255,null=True)
    HNT_REP_Date = models.CharField(max_length=255,null=True)
    HNT_REP_No = models.CharField(max_length=255,null=True)

    PT_REQ_Date = models.CharField(max_length=255,null=True)
    PT_REQ_No = models.CharField(max_length=255,null=True)
    # PT_Result = models.CharField(max_length=255,null=True)
    PT_REP_Date = models.CharField(max_length=255,null=True)
    PT_REP_No = models.CharField(max_length=255,null=True)

    MT_REQ_Date = models.CharField(max_length=255,null=True)
    MT_REQ_No = models.CharField(max_length=255,null=True)
    MT_REP_Date = models.CharField(max_length=255,null=True)
    MT_REP_No = models.CharField(max_length=255,null=True)

    HNT_REQ_Date = models.CharField(max_length=255,null=True)
    HNT_REQ_No = models.CharField(max_length=255,null=True)
    HNT_REP_Date = models.CharField(max_length=255,null=True)
    HNT_REP_No = models.CharField(max_length=255,null=True)
    HNT_Value = models.CharField(max_length=255,null=True)

    RT_Lenght = models.CharField(max_length=255,null=True)
    RT_Final_Result = models.CharField(max_length=255,null=True)

    UT_Lenght = models.CharField(max_length=255,null=True)
    UT_Final_Result = models.CharField(max_length=255,null=True)

    PWHT_REQ_Date = models.CharField(max_length=255,null=True)
    PWHT_REQ_No = models.CharField(max_length=255,null=True)
    PWHT_REP_Date = models.CharField(max_length=255,null=True)
    PWHT_REP_No = models.CharField(max_length=255,null=True)
    PWHT_Graph = models.ImageField(upload_to='general_welding', blank=True,null=True)

    Peaking_Before_Weld_Date = models.CharField(max_length=255,null=True)
    Peaking_Before_Weld_No = models.CharField(max_length=255,null=True)
    Peaking_Before_Weld_Value = models.CharField(max_length=255,null=True)
    Peaking_Before_Weld_Deviation = models.CharField(max_length=255,null=True)
    Peaking_After_Weld_Date = models.CharField(max_length=255,null=True)
    Peaking_After_Weld_No = models.CharField(max_length=255,null=True)
    Peaking_After_Weld_Value = models.CharField(max_length=255,null=True)
    Peaking_After_Weld_Deviation = models.CharField(max_length=255,null=True)

    Banding_Before_Weld_Date = models.CharField(max_length=255,null=True)
    Banding_Before_Weld_No = models.CharField(max_length=255,null=True)
    Banding_Before_Weld_Value = models.CharField(max_length=255,null=True)
    Banding_Before_Weld_Deviation = models.CharField(max_length=255,null=True)
    Banding_After_Weld_Date = models.CharField(max_length=255,null=True)
    Banding_After_Weld_No = models.CharField(max_length=255,null=True)
    Banding_After_Weld_Value = models.CharField(max_length=255,null=True)
    Banding_After_Weld_Deviation = models.CharField(max_length=255,null=True)


    doc_rev_1 = models.FileField(upload_to='doct',null=True,blank=True)
    doc_rev_2 = models.FileField(upload_to='doct',null=True,blank=True)
    doc_rev_3 = models.FileField(upload_to='doct',null=True,blank=True)
    doc_rev_4 = models.FileField(upload_to='doct',null=True,blank=True)
    doc_rev_5 = models.FileField(upload_to='doct',null=True,blank=True)

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    # def __str__(self):
    #     return self.row
    class Meta:
        verbose_name_plural = 'General Welding'
        ordering = ['row']


class GeneralPart(models.Model):
    row = models.CharField(max_length=255)
    tank = models.ForeignKey(Tank, related_name="G2_tanks",null=True, blank=False,on_delete=models.DO_NOTHING)
    DWG_No = models.CharField(max_length=255)

    Piece_Name= models.CharField(max_length=255,null=True)
    Piece_Code1 = models.CharField(max_length=255,null=True)
    Piece_No1 = models.CharField(max_length=255,null=True)
    Piece_Code2 = models.CharField(max_length=255,null=True)
    Piece_No2 = models.CharField(max_length=255,null=True)

    Material= models.CharField(max_length=255,null=True)
    Head_No = models.CharField(max_length=255,null=True)
    Thickness = models.CharField(max_length=255,null=True)
    Weight = models.CharField(max_length=255,null=True)
    Piece_No2 = models.CharField(max_length=255,null=True)

    Painting_Blasting_Surface_Aria = models.CharField(max_length=255,null=True)
    Painting_Blasting_Type = models.CharField(max_length=255,null=True)
    Painting_Blasting_Date = models.CharField(max_length=255,null=True)
    Painting_Blasting_No = models.CharField(max_length=255,null=True)

    Painting_Primer_Coat_Surface_Thickness = models.CharField(max_length=255,null=True)
    Painting_Primer_Coat_Surface_Date = models.CharField(max_length=255,null=True)
    Painting_Primer_Coat_Surface_No = models.CharField(max_length=255,null=True)

    Painting_Second_Coat_Surface_Thickness = models.CharField(max_length=255,null=True)
    Painting_Second_Coat_Surface_Date = models.CharField(max_length=255,null=True)
    Painting_Second_Coat_Surface_No = models.CharField(max_length=255,null=True)

    Painting_Third_Coat_Surface_Thickness = models.CharField(max_length=255,null=True)
    Painting_Third_Coat_Surface_Date = models.CharField(max_length=255,null=True)
    Painting_Third_Coat_Surface_No = models.CharField(max_length=255,null=True)

    Painting_Final_Coat_Surface_Thickness = models.CharField(max_length=255,null=True)
    Painting_Final_Coat_Surface_Date = models.CharField(max_length=255,null=True)
    Painting_Final_Coat_Surface_No = models.CharField(max_length=255,null=True)

    PMI_Date = models.CharField(max_length=255,null=True)
    PMINo = models.CharField(max_length=255,null=True)
    PMI_Result = models.CharField(max_length=255,null=True)

    Cutting_Date = models.CharField(max_length=255,null=True)
    Cutting_No = models.CharField(max_length=255,null=True)

    Bevelling_Date = models.CharField(max_length=255,null=True)
    Bevelling_No = models.CharField(max_length=255,null=True)

    MT_Date = models.CharField(max_length=255,null=True)
    MT_No = models.CharField(max_length=255,null=True)
    MT_Result = models.CharField(max_length=255,null=True)
    doc_rev_1 = models.FileField(upload_to='doct',null=True,blank=True)
    doc_rev_2 = models.FileField(upload_to='doct',null=True,blank=True)
    doc_rev_3 = models.FileField(upload_to='doct',null=True,blank=True)
    doc_rev_4 = models.FileField(upload_to='doct',null=True,blank=True)
    doc_rev_5 = models.FileField(upload_to='doct',null=True,blank=True)

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.row
    class Meta:
        verbose_name_plural = 'General Part'



class General(models.Model):
    row = models.CharField(max_length=255)
    tank = models.ForeignKey(Tank, related_name="General_tanks",null=True, blank=False,on_delete=models.DO_NOTHING)
    # tank_id = models.CharField(max_length=255)
    DWG_No = models.CharField(max_length=255)

    Joint_Course = models.CharField(max_length=255,null=True)
    Joint_No = models.CharField(max_length=255,null=True)
    Joint_Degree = models.CharField(max_length=255,null=True)

    Roundness_Before_Weld_Date =models.DateField()
    Roundness_Before_Weld_No = models.CharField(max_length=255,null=True)
    Roundness_Before_Weld_Value = models.CharField(max_length=255,null=True)
    Roundness_Before_Weld_Deviation = models.CharField(max_length=255,null=True)

    Roundness_After_Weld_Date = models.CharField(max_length=255,null=True)
    Roundness_After_Weld_No = models.CharField(max_length=255,null=True)
    Roundness_After_Weld_Value = models.CharField(max_length=255,null=True)
    Roundness_After_Weld_Deviation = models.CharField(max_length=255,null=True)

    Plumbness_Before_Weld_Date = models.CharField(max_length=255,null=True)
    Plumbness_Before_Weld_No = models.CharField(max_length=255,null=True)
    Plumbness_Before_Weld_Value = models.CharField(max_length=255,null=True)
    Plumbness_Before_Weld_Deviation = models.CharField(max_length=255,null=True)

    Plumbness_After_Weld_Date = models.CharField(max_length=255,null=True)
    Plumbness_After_Weld_No = models.CharField(max_length=255,null=True)
    Plumbness_After_Weld_Value = models.CharField(max_length=255,null=True)
    Plumbness_After_Weld_Deviation = models.CharField(max_length=255,null=True)

    Levelness_Before_Weld_Date = models.CharField(max_length=255,null=True)
    Levelness_Before_Weld_No = models.CharField(max_length=255,null=True)
    Levelness_Before_Weld_Value = models.CharField(max_length=255,null=True)
    Levelness_Before_Weld_Deviation = models.CharField(max_length=255,null=True)

    Levelness_After_Weld_Date = models.CharField(max_length=255,null=True)
    Levelness_After_Weld_No = models.CharField(max_length=255,null=True)
    Levelness_After_Weld_Value = models.CharField(max_length=255,null=True)
    Levelness_After_Weld_Deviation = models.CharField(max_length=255,null=True)
    doc_rev_1 = models.FileField(upload_to='doct',null=True,blank=True)
    doc_rev_2 = models.FileField(upload_to='doct',null=True,blank=True)
    doc_rev_3 = models.FileField(upload_to='doct',null=True,blank=True)
    doc_rev_4 = models.FileField(upload_to='doct',null=True,blank=True)
    doc_rev_5 = models.FileField(upload_to='doct',null=True,blank=True)

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    # class Meta:
    #     # ordering = ('name',)
    #     verbose_name = 'General'
    #     verbose_name_plural = 'Generals'

    def __str__(self):
        return self.row



class Rt(models.Model):

    row = models.CharField(max_length=255)

    # tank =models.ForeignKey(Tank, related_name="Rt",null=True, blank=False,on_delete=models.DO_NOTHING)
    tank =models.CharField(max_length=255,null=True,blank=True)
    location_1 = models.CharField(max_length=255,null=True,blank=True)
    location_2 = models.CharField(max_length=255,null=True,blank=True)
    joint_code_1 = models.CharField(max_length=255,null=True,blank=True)
    joint_no_1 = models.CharField(max_length=255,null=True,blank=True)
    joint_code_2 = models.CharField(max_length=255,null=True,blank=True)
    joint_no_2 = models.CharField(max_length=255,null=True,blank=True)

    Material_Specification	 = models.CharField(max_length=255,null=True,blank=True)
    Type_Of_Film = models.CharField(max_length=255,null=True,blank=True)
    Source_Type = models.CharField(max_length=255,null=True,blank=True)
    Density = models.CharField(max_length=255,null=True,blank=True)
    Decay_Chart = models.CharField(max_length=255,null=True,blank=True)
    SFD = models.CharField(max_length=255,null=True,blank=True)
    Exposure_Time = models.CharField(max_length=255,null=True,blank=True)
    Page = models.CharField(max_length=255,null=True,blank=True)
    I_Q_I_Type = models.CharField(max_length=255,null=True,blank=True)
    Sensitivity = models.CharField(max_length=255,null=True,blank=True)
    Tech = models.CharField(max_length=255,null=True,blank=True)
    Gamma_Ray = models.CharField(max_length=255,null=True,blank=True)
    RT_No = models.CharField(max_length=255,null=True,blank=True)
    Welder_Stamp = models.CharField(max_length=255,null=True,blank=True)
    Thk = models.CharField(max_length=255,null=True,blank=True)


    Req_RT_1ST_Date = models.CharField(max_length=255,null=True,blank=True)
    Req_RT_1ST_No = models.CharField(max_length=255,null=True,blank=True)
    Req_RT_Segment_From1 = models.CharField(max_length=255,null=True,blank=True)
    Req_RT_Segment_To1  = models.CharField(max_length=255,null=True,blank=True)

    # Req_RT_No = models.CharField(max_length=255)
    # Req_RT_Date = models.CharField(max_length=255)
    # Req_No = models.CharField(max_length=255)
    # Req_RT_Segment = models.CharField(max_length=255)

    Result_1ST_Date = models.CharField(max_length=255,null=True,blank=True)
    Result_1ST_No = models.CharField(max_length=255,null=True,blank=True)
    Result_1ST_Result = models.CharField(max_length=255,null=True,blank=True)
    Result_1ST_Defect = models.CharField(max_length=255,null=True,blank=True)
    Result_1ST_Segment = models.CharField(max_length=255,null=True,blank=True)

    Req_RT_2ND_Date = models.CharField(max_length=255,null=True,blank=True)
    Req_RT_2ND_No = models.CharField(max_length=255,null=True,blank=True)
    Req_2ND_Segment_From2 = models.CharField(max_length=255,null=True,blank=True)
    Req_2ND_Segment_To2  = models.CharField(max_length=255,null=True,blank=True)

    Result_2ND_Date = models.CharField(max_length=255,null=True,blank=True)
    Result_2ND_No = models.CharField(max_length=255,null=True,blank=True)
    Result_2ND_Result = models.CharField(max_length=255,null=True,blank=True)
    Result_2ND_Defect = models.CharField(max_length=255,null=True,blank=True)
    Result_2ND_Segment = models.CharField(max_length=255,null=True,blank=True)

    Req_RT_3RD_Date = models.CharField(max_length=255,null=True,blank=True)
    Req_RT_3RD_No = models.CharField(max_length=255,null=True,blank=True)
    Req_3RD_Segment_From2 = models.CharField(max_length=255,null=True,blank=True)
    Req_3RD_Segment_To2  = models.CharField(max_length=255,null=True,blank=True)

    Result_3RD_Date = models.CharField(max_length=255,null=True,blank=True)
    Result_3RD_No = models.CharField(max_length=255,null=True,blank=True)
    Result_3RD_Result = models.CharField(max_length=255,null=True,blank=True)
    Result_3RD_Defect = models.CharField(max_length=255,null=True,blank=True)
    Result_3RD_Segment = models.CharField(max_length=255,null=True,blank=True)


    Req_RT_4TH_No = models.CharField(max_length=255,null=True,blank=True)
    Req_RT_4TH_Date = models.CharField(max_length=255,null=True,blank=True)
    Req_4TH_Segment_From2 = models.CharField(max_length=255,null=True,blank=True)
    Req_4TH_Segment_To2  = models.CharField(max_length=255,null=True,blank=True)

    Result_4TH_Date = models.CharField(max_length=255,null=True,blank=True)
    Result_4TH_No = models.CharField(max_length=255,null=True,blank=True)
    Result_4TH_Result = models.CharField(max_length=255,null=True,blank=True)
    Result_4TH_Defect = models.CharField(max_length=255,null=True,blank=True)
    Result_4TH_Segment = models.CharField(max_length=255,null=True,blank=True)


    Req_RT_5TH_No = models.CharField(max_length=255,null=True,blank=True)
    Req_RT_5TH_Date = models.CharField(max_length=255,null=True,blank=True)
    Req_5TH_Segment_From2 = models.CharField(max_length=255,null=True,blank=True)
    Req_5TH_Segment_To2  = models.CharField(max_length=255,null=True,blank=True)

    Result_5TH_Date = models.CharField(max_length=255,null=True,blank=True)
    Result_5TH_No = models.CharField(max_length=255,null=True,blank=True)
    Result_5TH_Result = models.CharField(max_length=255,null=True,blank=True)
    Result_5TH_Defect = models.CharField(max_length=255,null=True,blank=True)
    Result_5TH_Segment = models.CharField(max_length=255,null=True,blank=True)


    Final_Result_Welder = models.CharField(max_length=255,null=True,blank=True)
    Final_Result_Joint = models.CharField(max_length=255,null=True,blank=True)


    doc_rev_1 = models.FileField(upload_to='doct',null=True,blank=True)
    doc_rev_2 = models.FileField(upload_to='doct',null=True,blank=True)
    doc_rev_3 = models.FileField(upload_to='doct',null=True,blank=True)
    doc_rev_4 = models.FileField(upload_to='doct',null=True,blank=True)
    doc_rev_5 = models.FileField(upload_to='doct',null=True,blank=True)
    confirmation=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)


    class Meta:
        verbose_name_plural = 'RT'
        ordering = ['row']


class Ut(models.Model):

    row = models.CharField(max_length=255)

        # tank =models.ForeignKey(Tank, related_name="Rt",null=True, blank=False,on_delete=models.DO_NOTHING)
    tank =models.CharField(max_length=255,null=True,blank=True)
    location_1 = models.CharField(max_length=255,null=True,blank=True)
    location_2 = models.CharField(max_length=255,null=True,blank=True)
    joint_code_1 = models.CharField(max_length=255,null=True,blank=True)
    joint_no_1 = models.CharField(max_length=255,null=True,blank=True)
    joint_code_2 = models.CharField(max_length=255,null=True,blank=True)
    joint_no_2 = models.CharField(max_length=255,null=True,blank=True)

    RT_No = models.CharField(max_length=255,null=True,blank=True)
    Req_RT_1ST_Date = models.CharField(max_length=255,null=True,blank=True)
    Req_RT_1ST_No = models.CharField(max_length=255,null=True,blank=True)
    Req_RT_Segment_From1 = models.CharField(max_length=255,null=True,blank=True)
    Req_RT_Segment_To1  = models.CharField(max_length=255,null=True,blank=True)

        # Req_RT_No = models.CharField(max_length=255)
        # Req_RT_Date = models.CharField(max_length=255)
        # Req_No = models.CharField(max_length=255)
        # Req_RT_Segment = models.CharField(max_length=255)

    Result_1ST_Date = models.CharField(max_length=255,null=True,blank=True)
    Result_1ST_No = models.CharField(max_length=255,null=True,blank=True)
    Result_1ST_Result = models.CharField(max_length=255,null=True,blank=True)
    Result_1ST_Defect = models.CharField(max_length=255,null=True,blank=True)
    Result_1ST_Segment = models.CharField(max_length=255,null=True,blank=True)

    Req_RT_2ND_Date = models.CharField(max_length=255,null=True,blank=True)
    Req_RT_2ND_No = models.CharField(max_length=255,null=True,blank=True)
    Req_2ND_Segment_From2 = models.CharField(max_length=255,null=True,blank=True)
    Req_2ND_Segment_To2  = models.CharField(max_length=255,null=True,blank=True)

    Result_2ND_Date = models.CharField(max_length=255,null=True,blank=True)
    Result_2ND_No = models.CharField(max_length=255,null=True,blank=True)
    Result_2ND_Result = models.CharField(max_length=255,null=True,blank=True)
    Result_2ND_Defect = models.CharField(max_length=255,null=True,blank=True)
    Result_2ND_Segment = models.CharField(max_length=255,null=True,blank=True)

    Req_RT_3RD_Date = models.CharField(max_length=255,null=True,blank=True)
    Req_RT_3RD_No = models.CharField(max_length=255,null=True,blank=True)
    Req_3RD_Segment_From2 = models.CharField(max_length=255,null=True,blank=True)
    Req_3RD_Segment_To2  = models.CharField(max_length=255,null=True,blank=True)

    Result_3RD_Date = models.CharField(max_length=255,null=True,blank=True)
    Result_3RD_No = models.CharField(max_length=255,null=True,blank=True)
    Result_3RD_Result = models.CharField(max_length=255,null=True,blank=True)
    Result_3RD_Defect = models.CharField(max_length=255,null=True,blank=True)
    Result_3RD_Segment = models.CharField(max_length=255,null=True,blank=True)


    Req_RT_4TH_No = models.CharField(max_length=255,null=True,blank=True)
    Req_RT_4TH_Date = models.CharField(max_length=255,null=True,blank=True)
    Req_4TH_Segment_From2 = models.CharField(max_length=255,null=True,blank=True)
    Req_4TH_Segment_To2  = models.CharField(max_length=255,null=True,blank=True)

    Result_4TH_Date = models.CharField(max_length=255,null=True,blank=True)
    Result_4TH_No = models.CharField(max_length=255,null=True,blank=True)
    Result_4TH_Result = models.CharField(max_length=255,null=True,blank=True)
    Result_4TH_Defect = models.CharField(max_length=255,null=True,blank=True)
    Result_4TH_Segment = models.CharField(max_length=255,null=True,blank=True)


    Req_RT_5TH_No = models.CharField(max_length=255,null=True,blank=True)
    Req_RT_5TH_Date = models.CharField(max_length=255,null=True,blank=True)
    Req_5TH_Segment_From2 = models.CharField(max_length=255,null=True,blank=True)
    Req_5TH_Segment_To2  = models.CharField(max_length=255,null=True,blank=True)

    Result_5TH_Date = models.CharField(max_length=255,null=True,blank=True)
    Result_5TH_No = models.CharField(max_length=255,null=True,blank=True)
    Result_5TH_Result = models.CharField(max_length=255,null=True,blank=True)
    Result_5TH_Defect = models.CharField(max_length=255,null=True,blank=True)
    Result_5TH_Segment = models.CharField(max_length=255,null=True,blank=True)


    Final_Result_Welder = models.CharField(max_length=255,null=True,blank=True)
    Final_Result_Joint = models.CharField(max_length=255,null=True,blank=True)


    doc_rev_1 = models.FileField(upload_to='doct',null=True,blank=True)
    doc_rev_2 = models.FileField(upload_to='doct',null=True,blank=True)
    doc_rev_3 = models.FileField(upload_to='doct',null=True,blank=True)
    doc_rev_4 = models.FileField(upload_to='doct',null=True,blank=True)
    doc_rev_5 = models.FileField(upload_to='doct',null=True,blank=True)
    confirmation=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    class Meta:
        verbose_name_plural = 'UT'

class WPS(models.Model):
    row = models.CharField(max_length=255)
    WPS_No = models.CharField(max_length=255)
    Type = models.CharField(max_length=255)

    t1 = models.CharField(max_length=255,null=True)
    t2 = models.CharField(max_length=255,null=True)
    t3 = models.CharField(max_length=255,null=True)
    t4 = models.CharField(max_length=255,null=True)
    t5 = models.CharField(max_length=255,null=True)
    t6 = models.CharField(max_length=255,null=True)
    t7 = models.CharField(max_length=255,null=True)
    t8 = models.CharField(max_length=255,null=True)
    t9 = models.CharField(max_length=255,null=True)
    t10 = models.CharField(max_length=255,null=True)

    t11 = models.CharField(max_length=255,null=True)
    t12 = models.CharField(max_length=255,null=True)
    t13 = models.CharField(max_length=255,null=True)
    t14 = models.CharField(max_length=255,null=True)
    t15 = models.CharField(max_length=255,null=True)
    t16 = models.CharField(max_length=255,null=True)
    t17 = models.CharField(max_length=255,null=True)
    t18 = models.CharField(max_length=255,null=True)
    t19 = models.CharField(max_length=255,null=True)
    t20 = models.CharField(max_length=255,null=True)

    t21 = models.CharField(max_length=255,null=True)
    t22 = models.CharField(max_length=255,null=True)
    t23 = models.CharField(max_length=255,null=True)
    t24 = models.CharField(max_length=255,null=True)
    t25 = models.CharField(max_length=255,null=True)
    t26 = models.CharField(max_length=255,null=True)
    t27 = models.CharField(max_length=255,null=True)
    t28 = models.CharField(max_length=255,null=True)
    t29 = models.CharField(max_length=255,null=True)
    t30 = models.CharField(max_length=255,null=True)

    t31 = models.CharField(max_length=255,null=True)
    t32 = models.CharField(max_length=255,null=True)
    t33 = models.CharField(max_length=255,null=True)
    t34 = models.CharField(max_length=255,null=True)
    t35 = models.CharField(max_length=255,null=True)
    t36 = models.CharField(max_length=255,null=True)
    t37 = models.CharField(max_length=255,null=True)
    t38 = models.CharField(max_length=255,null=True)
    t39 = models.CharField(max_length=255,null=True)
    t40 = models.CharField(max_length=255,null=True)

    t41 = models.CharField(max_length=255,null=True)
    t42 = models.CharField(max_length=255,null=True)
    t43 = models.CharField(max_length=255,null=True)
    t44 = models.CharField(max_length=255,null=True)
    t45 = models.CharField(max_length=255,null=True)
    t46 = models.CharField(max_length=255,null=True)
    t47 = models.CharField(max_length=255,null=True)
    t48 = models.CharField(max_length=255,null=True)
    t49 = models.CharField(max_length=255,null=True)
    t50 = models.CharField(max_length=255,null=True)
    class Meta:
        verbose_name_plural = 'WPS'

class PQR(models.Model):
    row = models.CharField(max_length=255)
    PQR_No = models.CharField(max_length=255)


    t1 = models.CharField(max_length=255,null=True)
    t2 = models.CharField(max_length=255,null=True)
    t3 = models.CharField(max_length=255,null=True)
    t4 = models.CharField(max_length=255,null=True)
    t5 = models.CharField(max_length=255,null=True)
    t6 = models.CharField(max_length=255,null=True)
    t7 = models.CharField(max_length=255,null=True)
    t8 = models.CharField(max_length=255,null=True)
    t9 = models.CharField(max_length=255,null=True)
    t10 = models.CharField(max_length=255,null=True)

    t11 = models.CharField(max_length=255,null=True)
    t12 = models.CharField(max_length=255,null=True)
    t13 = models.CharField(max_length=255,null=True)
    t14 = models.CharField(max_length=255,null=True)
    t15 = models.CharField(max_length=255,null=True)
    t16 = models.CharField(max_length=255,null=True)
    t17 = models.CharField(max_length=255,null=True)
    t18 = models.CharField(max_length=255,null=True)
    t19 = models.CharField(max_length=255,null=True)
    t20 = models.CharField(max_length=255,null=True)

    t21 = models.CharField(max_length=255,null=True)
    t22 = models.CharField(max_length=255,null=True)
    t23 = models.CharField(max_length=255,null=True)
    t24 = models.CharField(max_length=255,null=True)
    t25 = models.CharField(max_length=255,null=True)
    t26 = models.CharField(max_length=255,null=True)
    t27 = models.CharField(max_length=255,null=True)
    t28 = models.CharField(max_length=255,null=True)
    t29 = models.CharField(max_length=255,null=True)
    t30 = models.CharField(max_length=255,null=True)

    t31 = models.CharField(max_length=255,null=True)
    t32 = models.CharField(max_length=255,null=True)
    t33 = models.CharField(max_length=255,null=True)
    t34 = models.CharField(max_length=255,null=True)
    t35 = models.CharField(max_length=255,null=True)
    t36 = models.CharField(max_length=255,null=True)
    t37 = models.CharField(max_length=255,null=True)
    t38 = models.CharField(max_length=255,null=True)
    t39 = models.CharField(max_length=255,null=True)
    t40 = models.CharField(max_length=255,null=True)

    t41 = models.CharField(max_length=255,null=True)
    t42 = models.CharField(max_length=255,null=True)
    t43 = models.CharField(max_length=255,null=True)
    t44 = models.CharField(max_length=255,null=True)
    t45 = models.CharField(max_length=255,null=True)
    t46 = models.CharField(max_length=255,null=True)
    t47 = models.CharField(max_length=255,null=True)
    t48 = models.CharField(max_length=255,null=True)
    t49 = models.CharField(max_length=255,null=True)
    t50 = models.CharField(max_length=255,null=True)
    class Meta:
        verbose_name_plural = 'PQR'

# class Document(models.Model):
#     tank = models.ForeignKey(Tank, related_name="document_tank",null=True, blank=False,on_delete=models.DO_NOTHING)
#     first_image = models.ImageField(upload_to='tanks', blank=True)
#     second_image = models.ImageField(upload_to='tanks', blank=True)
#     third_image = models.ImageField(upload_to='tanks', blank=True)
#     fourth_image = models.ImageField(upload_to='tanks', blank=True)
#     fifth_image = models.ImageField(upload_to='tanks', blank=True)

# class Drawing(models.Model):
#
#     tank = models.ForeignKey(Tank, related_name="drawing_tanks",null=True, blank=False,on_delete=models.DO_NOTHING)
#     DWG_No = models.CharField(max_length=255)
#     file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
#
#     # ISO2 =  models.FileField(upload_to='iso/')
#     # ISO3 =  models.FileField(upload_to='iso/')
#     # ISO4 =  models.FileField(upload_to='iso/')
#     # ISO5 =  models.FileField(upload_to='iso/')
#     def __str__(self):
#         return self.DWG_No









# class Person(mdels.Model):
#     name = models.CharField(max_length=30)
#     email = models.EmailField(blank=True)
#     birth_date = models.DateField()
#     location = models.CharField(max_length=100, blank=True)

# class Person(models.Model):
#     name = models.CharField(max_length=100, verbose_name='full name')
#
#
#     def __str__(self):
#         return self.name
