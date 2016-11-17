from django.contrib import admin

from .forms import RuleForm
from .models import Rule, Profile


@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    """Admin for ``Rule`` model"""
    list_display = ('title',)
    form = RuleForm


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Admin for ``Profile`` model"""
    list_display = ('title',)
    filter_horizontal = ('rules',)
