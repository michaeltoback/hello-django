from tastypie.resources import ModelResource, ALL
import tastypie.fields
from hello.models import Legislator, Terms


class LegislatorResource(ModelResource):
    class Meta:
        queryset = Legislator.objects.all()
        allowed_methods = ['get']
        resource_name = 'legislator'
        filtering = {
                     'first_name': ALL,
                     'last_name':ALL,
                     }

class TermsResource(ModelResource):
    legislator = tastypie.fields.ToOneField(LegislatorResource, 'bioguide_id')
    class Meta:
        queryset = Terms.objects.all()
        resource_name = 'terms'
        allowed_methods = ['get']
        filtering = {
                     'terms_start': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
                     'terms_end':['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
                     'terms_state':ALL,
                     }


