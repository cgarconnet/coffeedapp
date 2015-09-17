from django.conf.urls import patterns, include, url
# from django.contrib import admin
import core.views as coreviews

urlpatterns = patterns('',

	url(r'^$', coreviews.LandingView.as_view()),
	url(r'location/$', coreviews.LocationListView.as_view()),

	# for url location/1/detail
	# $ to capture any wording after the url
	url(r'location/(?P<pk>\d+)/detail/$', coreviews.LocationDetailView.as_view(), name = 'location_list'),
	# name = 'location_list' has been added so we can use it into our Model and changing the label of details
	# has no longer impact on our other codes. Using it thru reverse function
)

