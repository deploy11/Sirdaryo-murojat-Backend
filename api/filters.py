import django_filters
from .models import Hokimiyat

class HokimiyatFilter(django_filters.FilterSet):
    class Meta:
        model = Hokimiyat
        fields = ['orinbosar', 'tashkilot','muddat',]