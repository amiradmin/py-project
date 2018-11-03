from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe
import os

# Create your models here.

class Project(models.Model):
    user = models.ForeignKey(get_user_model(), related_name="users",null=True, blank=False,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255, unique=True)
    owner = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contract_no = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True,blank=True)
    # created_by =  models.ForeignKey(settings.AUTH_USER_MODEL)


    def __str__(self):
        return self.name


class SubProject(models.Model):
    name = models.CharField(max_length=255, unique=True)
    project = models.ForeignKey(Project, related_name="project",null=True, blank=False,on_delete=models.DO_NOTHING)

    subcontractor = models.CharField(max_length=255)
    contractor = models.CharField(max_length=255)
    consultant = models.CharField(max_length=255,blank=True,null=True)
    tpa= models.CharField(max_length=255,blank=True,null=True)
    mc = models.CharField(max_length=255,blank=True,null=True)
    owner = models.CharField(max_length=255,blank=True)


    def __str__(self):
        return self.name

class DocumentFile(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, related_name="tank_project",null=True, blank=False,on_delete=models.DO_NOTHING)
    revision = models.CharField(max_length=255)
    file = models.FileField(upload_to='doct')
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    def image_tag(self):
        extension = os.path.splitext(self.file.name)[1]

        if extension=='.pdf':

            return mark_safe('<img src="/static/images/pdf.png" width="100" height="100"/> ')
        elif (extension=='.xls') or (extension=='.xlsx') :
            return mark_safe('<img src="/static/images/excel.png" width="130" height="100"/> ')
        elif (extension=='.doc') or (extension=='.docs') :
            return mark_safe('<img src="/static/images/word.png" width="100" height="100"/> ')
        else:
            return mark_safe('<img src="/media/%s" width="100" height="100"/> ' % (self.file))

    image_tag.short_description='Image'




    def __str__(self):
        return self.name
