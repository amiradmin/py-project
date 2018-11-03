from django.contrib import admin
from .models import Tank,GeneralWelding,GeneralPart,General,Rt,Ut,WPS,PQR
from import_export.admin import ImportExportModelAdmin



admin.site.register(WPS)

admin.site.site_header = 'Techinco'


class TankAdmin(admin.ModelAdmin):
    list_display = ['tank_no','title','inner_material','outer_material','inner_hight','outer_hight','inner_hight','outer_hight','inner_no_of_course','outer_no_of_course','inner_roof_type','outer_roof_type','inner_roof_shape','outer_roof_shape','subcontractor','contractor','tpa','mc','owner','doc_rev_1','doc_rev_2','doc_rev_3','doc_rev_4','doc_rev_5','created_at','updated_at']

admin.site.register(Tank, TankAdmin)

class GeneralAdmin(admin.ModelAdmin):
    list_display = ['row', 'DWG_No','tank','Joint_Course','Joint_No','Joint_Degree','Roundness_Before_Weld_Date','Roundness_Before_Weld_No','Roundness_Before_Weld_Value','Roundness_Before_Weld_Deviation','Roundness_After_Weld_Date','Roundness_After_Weld_No','Roundness_After_Weld_Value','Roundness_After_Weld_Deviation','Plumbness_Before_Weld_Date','Plumbness_Before_Weld_No','Plumbness_Before_Weld_Value','Plumbness_Before_Weld_Deviation','Plumbness_After_Weld_Date','Plumbness_After_Weld_No','Plumbness_After_Weld_Value','Plumbness_After_Weld_Deviation','doc_rev_1','doc_rev_2','doc_rev_3','doc_rev_4','doc_rev_5','created_at','updated_at']

admin.site.register(General, GeneralAdmin)

class GeneralWeldingAdmin(ImportExportModelAdmin):
    list_display = ['row','tank','location_1','location_2','joint_code_1','joint_no_1','joint_code_2','joint_no_2','thickness_1','thickness_2','wps_no','fitup_date','fitup_no','welder_1','welder_2','welder_3','welder_4','VBT_REQ_date','VBT_REQ_no','VBT_REP_date','VBT_REP_No','OilTest_REQ_Date','OilTest_REQ_No','OilTest_REP_Date','OilTest_REP_No','HNT_REQ_Date','HNT_REQ_No','HNT_REP_Date','HNT_REP_No','PT_REQ_Date','PT_REQ_No','PT_REP_Date','PT_REP_No','MT_REQ_Date','MT_REP_Date','MT_REP_No','RT_Lenght','RT_Final_Result','UT_Lenght','UT_Final_Result','PWHT_REQ_Date','PWHT_REQ_No','PWHT_REP_Date','PWHT_REP_No','PWHT_Graph','Peaking_Before_Weld_Date','Peaking_Before_Weld_No','Peaking_Before_Weld_Value','Peaking_Before_Weld_Deviation','Peaking_After_Weld_Date','Peaking_After_Weld_No','Peaking_After_Weld_Value','Peaking_After_Weld_Deviation','Banding_Before_Weld_Date','Banding_Before_Weld_No','Banding_Before_Weld_Value','Banding_Before_Weld_Deviation','Banding_After_Weld_Date','Banding_After_Weld_No','Banding_After_Weld_Value','Banding_After_Weld_Deviation','doc_rev_1','doc_rev_2','doc_rev_3','doc_rev_4','doc_rev_5','created_at','updated_at']

admin.site.register(GeneralWelding, GeneralWeldingAdmin)

class GeneralPartAdmin(admin.ModelAdmin):
    list_display = ['row','DWG_No','tank','Piece_Name','Piece_Code1','Piece_No1','Piece_Code2','Piece_No2','Material','Head_No','Thickness','Weight','Painting_Blasting_Surface_Aria','Painting_Blasting_Type','Painting_Blasting_Date','Painting_Blasting_No','Painting_Primer_Coat_Surface_Thickness','Painting_Primer_Coat_Surface_Date','Painting_Primer_Coat_Surface_No','Painting_Second_Coat_Surface_Thickness','Painting_Second_Coat_Surface_Date','Painting_Second_Coat_Surface_No','Painting_Third_Coat_Surface_Thickness','Painting_Third_Coat_Surface_Date','Painting_Third_Coat_Surface_No','Painting_Final_Coat_Surface_Thickness','Painting_Final_Coat_Surface_Date','Painting_Final_Coat_Surface_No','PMI_Date','PMINo','PMI_Result','Cutting_Date','Cutting_No','Bevelling_Date','Bevelling_No','MT_Date','MT_No','MT_Result','doc_rev_1','doc_rev_2','doc_rev_3','doc_rev_4','doc_rev_5','created_at','updated_at']


class RtAdmin(ImportExportModelAdmin):

    list_display=['row','tank','location_1','location_2','joint_code_1','joint_no_1','joint_code_2','joint_no_2','Material_Specification','Type_Of_Film','Source_Type','Density','Decay_Chart','SFD','Exposure_Time','Page','I_Q_I_Type','Sensitivity','Tech','Gamma_Ray','Welder_Stamp','Thk','Req_RT_1ST_No','Req_RT_1ST_Date','RT_No','Req_RT_Segment_From1','Req_RT_Segment_To1','Result_1ST_Date','Result_1ST_No','Result_1ST_Defect','Result_1ST_Segment','Result_1ST_Result','Req_RT_2ND_No','Req_RT_2ND_Date','Result_2ND_No','Result_2ND_Date','Result_2ND_Defect','Result_2ND_Segment','Result_2ND_Result','Req_RT_3RD_No','Req_RT_3RD_Date','Result_3RD_Date','Result_3RD_No','Result_3RD_Defect','Result_3RD_Segment','Result_3RD_Result','Req_RT_4TH_No','Req_RT_4TH_Date','Result_4TH_Date','Result_4TH_No','Result_4TH_Defect','Result_4TH_Segment','Result_4TH_Result','Req_RT_5TH_No','Req_RT_5TH_Date','Result_5TH_Date','Result_5TH_No','Result_5TH_Defect','Result_5TH_Segment','Result_5TH_Result','Final_Result_Welder','Final_Result_Joint','doc_rev_1','doc_rev_2','doc_rev_3','doc_rev_4','doc_rev_5','created_at','updated_at']
    list_filter = ['tank','location_1','location_2','joint_code_1','joint_no_1','joint_code_2','joint_no_2','Req_RT_1ST_No','Req_RT_1ST_Date','RT_No','Req_RT_Segment_From1','Req_RT_Segment_To1','doc_rev_1','doc_rev_2','doc_rev_3','doc_rev_4','doc_rev_5','created_at','updated_at']

class UtAdmin(ImportExportModelAdmin):

    list_display=['row','tank','location_1','location_2','joint_code_1','joint_no_1','joint_code_2','joint_no_2','Req_RT_1ST_No','Req_RT_1ST_Date','RT_No','Req_RT_Segment_From1','Req_RT_Segment_To1','Result_1ST_Date','Result_1ST_No','Result_1ST_Defect','Result_1ST_Segment','Result_1ST_Result','Req_RT_2ND_No','Req_RT_2ND_Date','Result_2ND_No','Result_2ND_Date','Result_2ND_Defect','Result_2ND_Segment','Result_2ND_Result','Req_RT_3RD_No','Req_RT_3RD_Date','Result_3RD_Date','Result_3RD_No','Result_3RD_Defect','Result_3RD_Segment','Result_3RD_Result','Req_RT_4TH_No','Req_RT_4TH_Date','Result_4TH_Date','Result_4TH_No','Result_4TH_Defect','Result_4TH_Segment','Result_4TH_Result','Req_RT_5TH_No','Req_RT_5TH_Date','Result_5TH_Date','Result_5TH_No','Result_5TH_Defect','Result_5TH_Segment','Result_5TH_Result','Final_Result_Welder','Final_Result_Joint','doc_rev_1','doc_rev_2','doc_rev_3','doc_rev_4','doc_rev_5','created_at','updated_at']
    list_filter = ['tank','location_1','location_2','joint_code_1','joint_no_1','joint_code_2','joint_no_2','Req_RT_1ST_No','Req_RT_1ST_Date','RT_No','Req_RT_Segment_From1','Req_RT_Segment_To1','doc_rev_1','doc_rev_2','doc_rev_3','doc_rev_4','doc_rev_5','created_at','updated_at']

admin.site.register(GeneralPart, GeneralPartAdmin)
admin.site.register(Rt,RtAdmin)
admin.site.register(Ut,UtAdmin)

admin.site.register(PQR)




# class BlogEntryOptions(admin.ModelAdmin):
#     formfield_overrides = {
#         models.ImageField: {'widget': FileInput},
#     }




# @admin.register(Person)
# class PersonAdmin(ImportExportModelAdmin):
#     pass
# class DocuemntAdmin(admin.ModelAdmin):

    # def save_model(self, request, obj, form, change):
    #     obj.save()
    #
    #     for afile in request.FILES.getlist('photos_multiple'):
    #         obj.photos.create(image=afile)
