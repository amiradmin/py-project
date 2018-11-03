"""techincopro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from  django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from .views import HomePage,Documents
from filebrowser.sites import site
from django.conf import settings
from controlcenter.views import controlcenter


urlpatterns = [

    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    # path('admin/filebrowser/', site.urls),
    # path('admin_tools/', include('admin_tools.urls')),
    path('admin/', admin.site.urls),
    path('projects/', include("projects.urls",namespace="projects")),
    path('tanks/', include("tanks.urls",namespace="tanks")),
    path('', HomePage.as_view(),name="home"),
    # path('tinymce/', include('tinymce.urls')),
    path('operators/', include("operators.urls",namespace="operators")),

    # path('accounts/', include('allauth.urls')),
    # path('admin/dashboard/', controlcenter.urls),



    # path('test/', include('filemanager.urls', namespace='filemanager')),


    # path('filer/', include('filer.urls')),

]
if settings.DEBUG: # will be 'True' in development
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
