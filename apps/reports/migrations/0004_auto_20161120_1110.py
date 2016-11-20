# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 11:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0002_profile'),
        ('reports', '0003_auto_20161114_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='onetimereport',
            name='total_rules',
            field=models.ManyToManyField(blank=True, related_name='one_time_reports_where_total', to='rules.Rule'),
        ),
        migrations.AddField(
            model_name='periodicreport',
            name='total_rules',
            field=models.ManyToManyField(blank=True, related_name='periodic_reports_where_total', to='rules.Rule'),
        ),
        migrations.AlterField(
            model_name='onetimereport',
            name='passed_rules',
            field=models.ManyToManyField(blank=True, related_name='one_time_reports_where_passed', to='rules.Rule'),
        ),
        migrations.AlterField(
            model_name='onetimereport',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='schedule.OneTimeTask'),
        ),
        migrations.AlterField(
            model_name='periodicreport',
            name='passed_rules',
            field=models.ManyToManyField(blank=True, related_name='periodic_reports_where_passed', to='rules.Rule'),
        ),
        migrations.AlterField(
            model_name='periodicreport',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='schedule.PeriodicTask'),
        ),
    ]