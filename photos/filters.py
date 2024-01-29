from .models import Photo
import django_filters
from django_filters import CharFilter

class PhotoFilter(django_filters.FilterSet):
    title = CharFilter(field_name="title", lookup_expr="icontains")
    description = CharFilter(field_name="description", lookup_expr="icontains")
    class Meta:
        model = Photo
        fields = ["title","area","lesson","status","description"]
