from django.shortcuts import render
import pickle
import os

# Create your views here.
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from numapp.models import HousingData
from numapp.forms import HousingDataForm

def HousingDataCreateView(request):

    if request.method == "POST":
        form = HousingDataForm(request.POST)

        if form.is_valid():
            X = list(form.cleaned_data.values())
            print([X])
            cwd = os.getcwd()
            filename = os.path.join(cwd, 'numapp', 'mlmodels', 'boston_final_model.sav')
            loaded_model = pickle.load(open(filename, 'rb'))
            result = loaded_model.predict([X])

        return render(request, 'numapp/housingdata_result.html', {'result': result})

    else:
        form = HousingDataForm()
        return render(request, 'numapp/housingdata_form.html', {'form': form})

def MlModelsView(request):
    return render(request, 'numapp/text.html')

#def HousingDataCreateView(CreateView):
#    model = HousingData
#    form_class = HousingDataForm

#    template_name = 'text/housingdata_form.html'

