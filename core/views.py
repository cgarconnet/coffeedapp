from django.shortcuts import render
from django.views.generic.base import TemplateView # to import html templates
from django.views.generic.list import ListView # to list my object from database
from django.views.generic.detail import DetailView # to show details of my selected object from database

import core.models as coremodels # we import our models

# Create your views here.

class LandingView(TemplateView):
		template_name = "base/index.html"

class LocationListView(ListView):
	# this is a template view that will show list
	model = coremodels.Location
	# template_name = "location/list.html"
	template_name = "location/list.html"

# let's create now a detailed view
class LocationDetailView(DetailView):
	# this is a template view that will show details
	model = coremodels.Location
	# template_name = "location/list.html"
	template_name = "location/detail.html"
	context_object_name = 'location'