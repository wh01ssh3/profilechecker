from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = (
    url(r'^', admin.site.urls),
    url(r'^api/auth/', include('rest_auth.urls', namespace='rest_framework')),
    url(r'^api/rules/', include('apps.rules.api.urls')),
)
