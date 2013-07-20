import os

from django.core.files.temp import NamedTemporaryFile
from django.core.files import File

from rest_framework import viewsets

from djazzle.core.models import Track
from djazzle.core.utils import reverse_track


class TrackViewSet(viewsets.ModelViewSet):
    model = Track

    def post_save(self, obj, created=False):
        super(TrackViewSet, self).post_save(obj, created)
        assert obj.data

        with NamedTemporaryFile(suffix='.mp3') as reversed_mp3:
            filename = os.path.splitext(obj.data.name)[0]
            obj.data.open()

            try:
                reverse_track(obj.data, reversed_mp3)
            finally:
                obj.data.close()

            reversed_mp3.seek(0)
            obj.reversed_data.save('%s_rev.mp3' % filename,
                                   File(reversed_mp3), save=True)
