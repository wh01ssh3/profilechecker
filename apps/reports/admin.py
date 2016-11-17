from django.contrib import admin

from .models import OneTimeReport, PeriodicReport


@admin.register(OneTimeReport)
@admin.register(PeriodicReport)
class ReportAdmin(admin.ModelAdmin):
    """Admin class for reports"""
    list_display = ('id', 'created', 'modified', 'task', 'passed_rules_count',
                    'total_rules_count')

    filter_horizontal = ('passed_rules',)

    readonly_fields = ('passed_rules', 'task')

    def has_add_permission(self, request):
        """Disallow to add reports through admin"""
        return False

    def passed_rules_count(self, obj):
        """Calculate passed rules"""
        return obj.passed_rules.count()

    def total_rules_count(self, obj):
        """Calculate total rules"""
        return obj.task.get_all_rules().count()
