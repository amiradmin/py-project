from django.shortcuts import render,get_object_or_404
from .models import Tank,GeneralWelding,GeneralPart,General,Rt
from django.contrib.auth.decorators import login_required
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.shortcuts import render
from django.urls import reverse_lazy ,reverse
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView,FormView

# Create your views here.
@login_required(login_url='/admin/login/')
def tanks_selected_list(request, id):

    tanks = Tank.objects.filter(id=id)

    return render(request,
                  'tanks_list.html',
                  {'tanks': tanks},

                   )
@login_required(login_url='/admin/login/')

def tanks_list(request):

    tanks = Tank.objects.all()

    return render(request,
                  'tanks_list.html',
                  {'tanks': tanks},

                   )
@login_required(login_url='/admin/login/')

def tanks_list_photo(request, id):

    tanks_photo = Tank.objects.all()

    return render(request,
                  'photo_list.html',
                  {'tanks_photo': tanks_photo},

                   )

@login_required(login_url='/admin/login/')
def general_welding_list(request, id):

    general_weldings = GeneralWelding.objects.all()

    return render(request,
                  'general_welding_list.html',
                  {'general_weldings': general_weldings},

                   )

@login_required(login_url='/admin/login/')
def general_welding_detail(request, id):

    gw = get_object_or_404(GeneralWelding,
                            id=id)
    return render(request,
              'general_welding_details.html',
              {'gw': gw})
@login_required(login_url='/admin/login/')
def general_part_detail(request, id):

    gp = get_object_or_404(GeneralPart,
                            id=id)
    return render(request,
              'general_part_detail.html',
              {'gp': gp })

@login_required(login_url='/admin/login/')
def general_detail(request, id):

    general = get_object_or_404(General,
                            id=id)
    return render(request,
              'general_detail.html',
              {'general': general })
@login_required(login_url='/admin/login/')
def graph_show(request, id):

    graph = get_object_or_404(GeneralWelding,
                            id=id)
    return render(request,
              'graph.html',
              {'graph': graph })

# @login_required(login_url='/admin/login/')
# def rt_list(request, tank):
#
#     rts = Rt.objects.all()
#
#     return render(request,
#                   'rt_list.html',
#                   {'rts': rts},
#
#                    )

# @login_required(login_url='/admin/login/')
# def rt_details(request, row):
#
#     rt_detail = get_object_or_404(Rt,
#                             row=row)
#     return render(request,
#               'rt_detail.html',
#               {'rt_detail': rt_detail })


class RtListView(ListView):
    model = Rt
    template_name='tanks/rt_list.html'
    context_object_name='rtlist'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(tank__iexact = self.kwargs.get("tank"))

class RtListViewForm(ListView):
    model = Rt
    template_name='tanks/rt_list_form.html'
    context_object_name='rtlistform'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(tank__iexact = self.kwargs.get("tank"))

class RtConfirmUpdate(UpdateView):
    model = Rt
    fields = ['confirmation']

    template_name='rt_confirm.html'


    def get_success_url(self):

        return reverse('tanks:rt_list', kwargs={'tank': self.get_object().tank})
