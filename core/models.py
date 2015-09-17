from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
# be careful, not doing copy/paste, use Tab
# this will show that we are in the same object
# avoid any spaces

class Location(models.Model):
	title = models.CharField(max_length=300)
 	description = models.TextField(null=True, blank=True) 
 	created_at = models.DateTimeField(auto_now_add=True)

 	def __unicode__(self):
 		return self.title
 		
 	def get_absolute_url(self):
 		# return "location/"+str(self.id)+"/detail" # not the best way to do it
 		# instead use the core.urlresolvers
 		return reverse (viewname="location_list", args=[self.id])

