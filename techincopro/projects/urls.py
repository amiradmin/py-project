from django.conf.urls import url, include
from . import views

app_name = 'projects'
urlpatterns = [
    url(r"^$", views.ProjectList.as_view(), name="project_list"),
    url(r"^sub$", views.subproject_list, name="subproject_list"),
    url(r'^(?P<id>\d+)/(?P<project_id>\d+)$', views.subproject_detail, name='subproject_detail'),
    url(r'^doclist/', views.DocumentListView.as_view(), name='doc_list_'),
    ]
# (?P<slug>[-\w]+)
