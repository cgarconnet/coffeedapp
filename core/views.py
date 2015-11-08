from django.shortcuts import render
from django.views.generic.base import TemplateView # to import html templates
from django.views.generic.list import ListView # to list my object from database
from django.views.generic.detail import DetailView # to show details of my selected object from database
from django.views.generic.edit import CreateView, UpdateView # to enable the edit form (create and then edit)
from sitegate.decorators import redirect_signedin, sitegate_view # for sitegate and authenficiation

# from django.contrib.auth.decorators import user_passes_test

import core.models as coremodels # we import our models
	
# Create your views here.

class LandingView(TemplateView):
		template_name = "base/index.html"

class LocationListView(ListView):
	# this is a template view that will show list
	model = coremodels.Location
	# template_name = "location/list.html"
	template_name = "location/list.html"
	paginate_by = 4 # definition of max py page


class SearchListView(LocationListView):
	# this is a search view that herit from LocationListView and not directly from ListView 

	def get_queryset(self):
		incoming_query_string = self.request.GET.get('query', '') # query is the name defined in the form
		return coremodels.Location.objects.filter(title__icontains=incoming_query_string)

# let's create now a detailed view
class LocationDetailView(DetailView):
	# this is a template view that will show details
	model = coremodels.Location
	# template_name = "location/list.html"
	template_name = "location/detail.html"
	context_object_name = 'location'

	def get_context_data(self, **kwargs):
		# the reverse as form_valid. Modify data between extract from DB -> page
		context = super(LocationDetailView, self).get_context_data(**kwargs)
		location = coremodels.Location.objects.get(id=self.kwargs['pk'])

		if self.request.user.is_authenticated():
			user_reviews = coremodels.Review.objects.filter(location=location, user=self.request.user)
			if user_reviews.count() > 0:
				context['user_review'] = user_reviews[0]
			else:
				context['user_review'] = None
		return context


class LocationCreateView(CreateView):
	model = coremodels.Location
	template_name = 'base/form.html'
	fields ="__all__"

# @user_passes_test(lambda u:u.is_staff, login_url='/entrance/')
class LocationUpdateView(UpdateView):
	model = coremodels.Location
	template_name = 'base/form.html'
	fields ="__all__"


class ReviewCreateView(CreateView):
	model = coremodels.Review # by just changing the model here, I can have access to the right form edit template
	template_name = 'base/form.html'
	# fields ="__all__" this is when we want all fields, but in this case, we don't want the user nor the Location Id
	fields = ['description', 'rating']

	def form_valid(self, form):
	# this feature is used between submission of the user and sending these data to the database
		form.instance.user = self.request.user
		form.instance.location = coremodels.Location.objects.get(id=self.kwargs['pk'])
		return super(ReviewCreateView, self).form_valid(form)

	def get_success_url(self): # returning the url of what we just edited
		return self.object.location.get_absolute_url()


class ReviewUpdateView(UpdateView):
	model = coremodels.Review # by just changing the model here, I can have access to the right form edit template
	template_name = 'base/form.html'
	# fields ="__all__" this is when we want all fields, but in this case, we don't want the user nor the Location Id
	fields = ['description', 'rating']

	def get_object(self):
		# return the review object for the current user and the current location
		return coremodels.Review.objects.get(location__id=self.kwargs['pk'], user=self.request.user)

	def get_success_url(self): # returning the url of what we just edited
		return self.object.location.get_absolute_url()

# code for site authentification
# only specific here is the name of entrance page
@sitegate_view(widget_attrs={'class': 'form-control', 'placeholder': lambda f: f.label}, template='form_bootstrap3') # This also prevents logged in users from accessing our sign in/sign up page.
def entrance(request):
	return render(request, 'base/entrance.html', {'title': 'Sign in & Sign up'})
