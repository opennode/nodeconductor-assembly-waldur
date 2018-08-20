from __future__ import unicode_literals

from django.contrib import admin
from django.forms.models import ModelForm
from jsoneditor.forms import JSONEditor

from . import models


class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'customer', 'created')


class AttributeOptionInline(admin.TabularInline):
    model = models.AttributeOption


class AttributeAdmin(admin.ModelAdmin):
    inlines = [AttributeOptionInline]
    list_display = ('title', 'section', 'type')
    ordering = ('section', 'title')


class AttributeInline(admin.TabularInline):
    model = models.Attribute


class SectionAdmin(admin.ModelAdmin):
    inlines = [AttributeInline]


class SectionInline(admin.TabularInline):
    model = models.Section


class CategoryAdmin(admin.ModelAdmin):
    inlines = [SectionInline]


class ScreenshotsInline(admin.TabularInline):
    model = models.Screenshots


class PlansInline(admin.TabularInline):
    model = models.Plan


class OfferingAdminForm(ModelForm):
    class Meta:
        widgets = {
            'attributes': JSONEditor(),
            'geolocations': JSONEditor(),
        }


class OfferingAdmin(admin.ModelAdmin):
    form = OfferingAdminForm
    inlines = [ScreenshotsInline, PlansInline]
    fields = ('is_active', 'category', 'name', 'native_name',
              'description', 'native_description', 'full_description',
              'rating', 'thumbnail', 'attributes', 'geolocations',
              'vendor_details', 'scope')
    readonly_fields = ('rating', 'scope')


class OrderItemInline(admin.TabularInline):
    model = models.OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'project', 'created', 'state', 'total_cost')
    list_filter = ('state',)
    inlines = [OrderItemInline]


admin.site.register(models.ServiceProvider, ServiceProviderAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Offering, OfferingAdmin)
admin.site.register(models.Section, SectionAdmin)
admin.site.register(models.Attribute, AttributeAdmin)
admin.site.register(models.Screenshots)
admin.site.register(models.Order, OrderAdmin)
