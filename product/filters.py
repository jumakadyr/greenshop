import django_filters
from .models import Plant, Category
from .choices import *

class PlantFilter(django_filters.FilterSet):
    category = django_filters.ModelMultipleChoiceFilter(
        field_name="categories",
        queryset=Category.objects.all(),
        to_field_name="id",
    )
    max_price = django_filters.NumberFilter(
        field_name="price",
        lookup_expr="gte",
    )
    min_price = django_filters.NumberFilter(
        field_name="price",
        lookup_expr="lte",
    )
    class Meta:
        model = Plant
        fields = ['category', 'max_price', 'min_price']

class PlantSizeFilter(django_filters.FilterSet):
    category = django_filters.ModelMultipleChoiceFilter(
        field_name="categories",
        queryset=Category.objects.all(),
        to_field_name="id",
    )
    size = django_filters.ModelMultipleChoiceFilter(
        field_name="sizes",
        choices=PlantSizeChoices.choices
    )

    class Meta:
        model = Plant
        fields = ['category', 'size']

