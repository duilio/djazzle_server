from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework import routers

from djazzle.core.views import TrackViewSet
from djazzle.core.views import TrackViewRandom
from djazzle.core.views import Style
from djazzle.core.views	import artistlist
from djazzle.core.views	import topSong




router = routers.DefaultRouter()
router.register(r'tracks', TrackViewSet)


router.register(r'trackRandom', TrackViewRandom)

router.register(r'style',Style)


router.register(r'artistlist',artistlist)

router.register(r'topsong',topSong)



admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        # ... the rest of your URLconf goes here ...
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
