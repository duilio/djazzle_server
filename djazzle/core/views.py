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


		




		







