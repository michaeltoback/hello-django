from tastypie.resources import ModelResource, ALL
from hello.models import Legislator, Terms

class LegislatorResource(ModelResource):
    class Meta:
        queryset = Legislator.objects.all()
        resource_name = 'legislator'
        filtering = {
                     'first_name': ALL,
                     'last_name':ALL,
                     }