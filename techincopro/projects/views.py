from django.shortcuts import render, get_object_or_404
from .models import Project,SubProject,DocumentFile
from django.views.generic import ListView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.


class ProjectList(LoginRequiredMixin,ListView):
    model = models.Project
    login_url = '/admin/login/'
    template_name = "projects_list.html"

# class SubProjectList(ListView):
#     model = models.SubProject
#     template_name = "subproject_list.html"
@login_required(login_url='/admin/login/')
def subproject_list(request):

    subprojects = SubProject.objects.all()

    return render(request,
                  'subproject_list.html',
                  {'subprojects': subprojects},

                   )

@login_required(login_url='/admin/login/')
def subproject_detail(request, id,project_id):

    subprojects = SubProject.objects.filter(id=id)
    request.session['proname'] =project_id

    return render(request,
                  'subproject_list.html',
                  {'subprojects': subprojects},

                   )

class DocumentListView(ListView):
    model = DocumentFile
    template_name='documents.html'
    context_object_name='documentlist'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        proname = self.request.session['proname']
        return queryset.filter(project =proname)
