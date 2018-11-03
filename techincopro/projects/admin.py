from django.contrib import admin
from .models import Project,SubProject,DocumentFile
from django.contrib.auth.models import Group

# Register your models here.
# admin.site.register(Project)
# admin.site.register(SubProject)



class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name','owner','location','contract_no','description']

    def get_queryset(self, request):
        one=Group.objects.get(name="SPG").user_set.all()
        qs = super(ProjectAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.all()
        elif request.user in one :
            return qs.filter(user=request.user)
        else:
            # Must find a new way here
         return qs.filter(user=request.user)
admin.site.register(Project, ProjectAdmin)


class SubrojectAdmin(admin.ModelAdmin):
    list_display = ['name','subcontractor','contractor','consultant','tpa','mc','owner']

admin.site.register(SubProject, SubrojectAdmin)


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('image_tag','name','project','revision','created_at')
    readonly_fields=['image_tag']
    list_filter = ['name','revision','project','created_at']

admin.site.register(DocumentFile,DocumentAdmin)
