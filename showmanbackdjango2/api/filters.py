from django_filters import rest_framework as filters
from api.models import EventTypes1, Orders1


class EventFilter(filters.FilterSet):
    # name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = EventTypes1
        fields = ('id', 'event_title',)


class OrderFilter(filters.FilterSet):

    class Meta:
        model = Orders1
        fields = ('id',)