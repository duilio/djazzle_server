from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

from djazzle.core.views import TrackViewSet


router = routers.DefaultRouter()
router.register(r'tracks', TrackViewSet)


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth', include('rest_framework.urls', namespace='rest_framework')),
)
