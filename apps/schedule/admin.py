from django.contrib import admin

from .models import OneTimeTask, PeriodicTask


@admin.register(OneTimeTask)
class OneTimeTaskAdmin(admin.ModelAdmin):
    """Admin for ``OneTimeTask`` model"""
    list_display = ('id', 'title', 'time', 'rules_count', 'profiles_count')
    filter_horizontal = ('rules', 'profiles')
    list_filter = ('time',)
    search_fields = ('title',)

    def rules_count(self, obj):
        """Calculate count of ``rules``"""
        return obj.rules.count()

    def profiles_count(self, obj):
        """Calculate count of ``profiles``"""
        return obj.profiles.count()


@admin.register(PeriodicTask)
class PeriodicTaskAdmin(OneTimeTaskAdmin):
    """Admin for ``PeriodicTask`` model"""
    list_display = (
        'id', 'title', 'every', 'metric', 'rules_count', 'profiles_count',
        'created', 'modified')
    list_filter = ('created', 'modified', 'metric')
