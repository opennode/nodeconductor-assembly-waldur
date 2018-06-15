from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from django.db.models import OuterRef, Subquery
from rest_framework.settings import api_settings

from waldur_core.core import filters as core_filters
from waldur_core.structure import filters as structure_filters
from waldur_core.structure import models as structure_models

from . import models


class PriceEstimateScopeFilterBackend(core_filters.GenericKeyFilterBackend):

    def get_related_models(self):
        return models.PriceEstimate.get_estimated_models()

    def get_field_name(self):
        return 'scope'


class CustomerEstimatedCostFilter(core_filters.BaseExternalFilter):
    def filter(self, request, queryset, view):

        order_by = request.query_params.get(api_settings.ORDERING_PARAM)
        if order_by not in ('estimated_cost', '-estimated_cost'):
            return queryset

        ct = ContentType.objects.get_for_model(structure_models.Customer)
        estimates = models.PriceEstimate.objects.filter(content_type=ct, object_id=OuterRef('pk'))
        queryset = queryset.annotate(estimated_cost=Subquery(estimates.values('total')[:1]))
        queryset = queryset.order_by(order_by)
        return queryset


structure_filters.ExternalCustomerFilterBackend.register(CustomerEstimatedCostFilter())
