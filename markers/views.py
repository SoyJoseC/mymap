from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView

class MarkerView(TemplateView):
    """ Markers map view. """

    template_name = "map.html"