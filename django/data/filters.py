import django_filters

from .models import Data


class DataFilter(django_filters.FilterSet):
    class Meta:
        model = Data
        fields = ['id', 'text', 'label']
