from django.db import models
from rest_framework import serializers as rf_serializers


class UsageMixin(models.Model):
    class Meta:
        abstract = True

    cpu_usage = models.BigIntegerField(default=0)
    ram_usage = models.BigIntegerField(default=0)
    gpu_usage = models.BigIntegerField(default=0)


class AllocationUsageSerializerMixin(rf_serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UsageMixin
        fields = (
            'cpu_usage',
            'ram_usage',
            'gpu_usage',
            'month',
            'year',
        )
