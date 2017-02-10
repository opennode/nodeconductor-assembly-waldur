import django_filters

from nodeconductor.core import filters as core_filters

from . import models


class PackageTemplateFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_type='icontains')
    service_settings = core_filters.URLFilter(
        view_name='servicesettings-detail', name='service_settings__uuid')
    service_settings_uuid = django_filters.UUIDFilter(name='service_settings__uuid')
    openstack_package_service_settings = core_filters.URLFilter(
        view_name='servicesettings-detail', name='openstack_packages__service_settings__uuid')
    openstack_package_service_settings_uuid = django_filters.UUIDFilter(
        name='openstack_packages__service_settings__uuid')

    class Meta(object):
        model = models.PackageTemplate


class OpenStackPackageFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_type='icontains')
    customer = core_filters.URLFilter(
        view_name='customer-detail', name='tenant__service_project_link__project__customer__uuid')
    customer_uuid = django_filters.UUIDFilter(name='tenant__service_project_link__project__customer__uuid')
    project = core_filters.URLFilter(
        view_name='project-detail', name='tenant__service_project_link__project__uuid')
    project_uuid = django_filters.UUIDFilter(name='tenant__service_project_link__project__uuid')
    tenant = core_filters.URLFilter(view_name='openstack-tenant-detail', name='tenant__uuid')
    tenant_uuid = django_filters.UUIDFilter(name='tenant__uuid')
    service_settings = core_filters.URLFilter(
        view_name='servicesettings-detail', name='service_settings__uuid')
    service_settings_uuid = django_filters.UUIDFilter(name='service_settings__uuid')

    class Meta(object):
        model = models.OpenStackPackage
