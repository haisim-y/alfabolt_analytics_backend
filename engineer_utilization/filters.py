import django_filters
from .models import Resource
import logging

class DashboardFilter(django_filters.FilterSet):
    technology_name=django_filters.CharFilter(field_name='projectresource__project__title',lookup_expr='iecxact')
    project_title=django_filters.CharFilter(field_name='resourcetechnology__technology__name',lookup_expr='icontains')
    #resource_level=django_filters.CharFilter(field_name='level',lookup_expr='iexact')

    class Meta:
        model=Resource
        fields=['level']
    def filter_technology_name(self, queryset, name, value):
        return queryset.filter(resourcetechnology__technology__name__iexact=value)

    def filter_project_title(self, queryset, name, value):
        return queryset.filter(projectresource__project__title__iexact=value)

    def filter_resource_level(self, queryset, name, value):
        return queryset.filter(level__iexact=value)





