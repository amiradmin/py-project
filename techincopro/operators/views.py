from django.shortcuts import render
from .models import Operator
from .forms import OperatorForm
from django.shortcuts import redirect
# Create your views here.

def get_operators(request):
    if request.method == "POST":
        form = OperatorForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('projects:project_list')

    else :
        form = OperatorForm()


    return render(request,'operators/operator_form.html',{'form':form})
