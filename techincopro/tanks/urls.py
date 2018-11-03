from django.conf.urls import url, include
from django.urls import path
from tanks import views

app_name = 'tanks'
urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.tanks_selected_list, name='tanks_selected_list'),
    url(r'lg/(?P<id>\d+)/$', views.general_welding_list, name='general_welding_list'),
    url(r'gwdetails/(?P<id>\d+)/$', views.general_welding_detail, name='general_welding_detail'),
    url(r'gpdetails/(?P<id>\d+)/$', views.general_part_detail, name='general_part_detail'),
    url(r'generaldetails/(?P<id>\d+)/$', views.general_detail, name='general_detail'),
    url(r'graph/(?P<id>\d+)/$', views.graph_show, name='graph_show'),
    url(r'tankslist/$', views.tanks_list, name='tanks_list'),
    url(r'tanksphoto/(?P<id>\d+)/$', views.tanks_list_photo, name='tanks_photo_list_'),
    url(r'^rtlist/(?P<tank>.+)$', views.RtListView.as_view(), name='rt_list'),
    url(r'^rtlistform/(?P<tank>.+)$', views.RtListViewForm.as_view(), name='rt_list_form'),
    # url(r'rtdetail/(?P<row>\d+)/$', views.rt_details, name='rt_detail_'),
    url(r'rtconfirm/(?P<pk>\d+)/$', views.RtConfirmUpdate.as_view(), name='rt_confirm_'),

    # path('rtlist', views.RtListView.as_view(), name='rt-list'),
    # url(r'^rtlist/(?P<tank>.+)$', views.RtListView.as_view(), name='rt_list'),
    # url(r'^rtlist/', views.people, name='rt_list'),



    ]
