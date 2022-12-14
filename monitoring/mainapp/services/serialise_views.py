from django.db.models import Max
from django.db.models import QuerySet
from mainapp.models import DataCoordinates


def queryset_last_location() -> QuerySet:
    """forming QuerySet with data last locations transport"""
    transport_list = []
    time_list = []
    query = DataCoordinates.objects.values('transport_id').annotate(latest=Max('add_datetime'))
    for i in query:
        time_list.append(i['latest'])
        transport_list.append(i['transport_id'])
    return DataCoordinates.objects.prefetch_related('transport').\
        filter(transport_id__in=transport_list).filter(add_datetime__in=time_list)