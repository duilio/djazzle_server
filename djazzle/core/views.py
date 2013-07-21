import os

from django.core.files.temp import NamedTemporaryFile
from django.core.files import File

from rest_framework import viewsets
import requests
from djazzle.core.models import Track
from djazzle.core.models import TrackRandomDeezer
from djazzle.core.models import StyleType
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from djazzle.core.models import artistsList
from djazzle.core.models import topSongArtistUser
from djazzle.core.utils import reverse_track


class TrackViewSet(viewsets.ModelViewSet):	
    model = Track


class TrackViewRandom(viewsets.ModelViewSet):
	model = TrackRandomDeezer 

class Style (viewsets.ModelViewSet):
	model = StyleType()
	a = model.popolateStyle()
	model.getGender()
	models = StyleType

class artistlist(viewsets.ModelViewSet):
	a = artistsList()
	a.populate()
	model = artistsList

class topSong(viewsets.ModelViewSet):
	top = topSongArtistUser()
	top.populateTop()
	model = topSongArtistUser


		




		







=======
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
>>>>>>> d8e36c77da27e7f355d507656076cbfc10a3e2ac
