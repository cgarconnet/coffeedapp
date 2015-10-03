from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required # to block users who are not logged is so that cannot create
# all url that we want to protect we add login_required()

# from django.contrib import admin
import core.views as coreviews

urlpatterns = patterns('',

	url(r'^$', coreviews.LandingView.as_view()),
	url(r'location/$', coreviews.LocationListView.as_view()),

	# Registering the url for search
	url(r'search/$', coreviews.SearchListView.as_view()),


	# for url location/1/detail
	# pk stands for Primary Key
	# $ to capture any wording after the url
	url(r'location/(?P<pk>\d+)/detail/$', coreviews.LocationDetailView.as_view(), name = 'location_list'),
	# name = 'location_list' has been added so we can use it into our Model and changing the label of details
	# has no longer impact on our other codes. Using it thru reverse function

	url(r'location/create/$', login_required(coreviews.LocationCreateView.as_view())),
	# LocationCreateView isa name we defined in views.py in the Core folder


	url(r'location/(?P<pk>\d+)/update/$', login_required(coreviews.LocationUpdateView.as_view()), name = 'location_update'),


	#now the url to create and update a review
	url(r'location/(?P<pk>\d+)/review/create/$', login_required(coreviews.ReviewCreateView.as_view()), name = 'review_create'),
	url(r'location/(?P<pk>\d+)/review/update/$', login_required(coreviews.ReviewUpdateView.as_view()), name = 'review_update'),


	# Registering the entrance login page
	url(r'entrance/$', coreviews.entrance),

	# easy url to logout
	url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/entrance'})
		# next page coulb be our /entrance
)

