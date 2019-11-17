from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import FormView

from .forms import SampleForm

class SampleView(FormView):

    form_class = SampleForm
    template_name = 'sample.html'