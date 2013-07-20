from django.conf.urls import patterns, include, url
from rest_framework import routers

router = routers.DefaultRouter()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth', include('rest_framework.urls', namespace='rest_framework')),
)
