from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Profile Checker API')

urlpatterns = (
    url(r'^', admin.site.urls),
    url(r'^swagger/', schema_view),
    url(r'^api/auth/', include('rest_auth.urls', namespace='rest_framework')),
    url(r'^api/rules/', include('apps.rules.api.urls')),
    url(r'^api/schedule/', include('apps.schedule.api.urls')),
    url(r'^api/reports/', include('apps.reports.api.urls')),
)
