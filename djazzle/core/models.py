from django.db import models
import requests



class Track(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    data = models.FileField(upload_to='tracks/')

class TrackRandomDeezer(models.Model):
	ids = models.IntegerField()
	author = models.CharField(max_length=200)
	linkSong = models.CharField(max_length=200)

class StyleType(models.Model):
	ids = models.IntegerField()
	name = models.CharField(max_length=200)
	types = models.CharField(max_length=200)


	def popolateStyle(self):
		r = requests.get("https://api.deezer.com/2.0/genre")
		listOfstyle = r.json()		
		for item in listOfstyle['data']:
			genesis =  StyleType.objects.create(ids=item.values()[1],name=item.values()[2],types=item.values()[0])
			genesis.save()

	def getGender(self):
		query = StyleType.objects.filter(name = u'Metal')
		r = requests.get("https://api.deezer.com/2.0/genre/1057/artists")

class artistsList(models.Model):
	  ids = models.IntegerField()
	  

	  def populate(self):
	      r = requests.get("https://api.deezer.com/2.0/genre/1057/artists")
	      listOfstyle = r.json()
	      for item in listOfstyle['data']:
	      	query = artistsList.objects.create(ids=item.values()[3])
	      	query.save()

class topSongArtist(models.Model):
	   preview = models.CharField(max_length=200)
	   ids = models.CharField(max_length=200)
	  

	   def populateTop(self):
	   	   r = requests.get("https://api.deezer.com/2.0/artist/1182/top")
	   	   listOfstyle = r.json()
	   	   for item in listOfstyle['data']:
	      		query = topSongArtist.objects.create(ids=item.values()[8], preview=item.values()[7])
	      		query.save()


class topSongArtistUser(models.Model):
	   preview = models.CharField(max_length=200)
	   ids = models.CharField(max_length=200)

	   
	   def populateTop(self):
	   	  r = requests.get("https://api.deezer.com/2.0/artist/1182/top")
	   	  listOfstyle = r.json()
	   	  for item in listOfstyle['data']:
	      	    query = topSongArtist.objects.create(ids=item.values()[8], preview=item.values()[7])
	      	    query.save()

	   	   














					




=======
    reversed_data = models.FileField(upload_to='reverse_tracks/', null=True, blank=True)
>>>>>>> d8e36c77da27e7f355d507656076cbfc10a3e2ac
