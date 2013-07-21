import urllib2
from djazzle.core.models import topSongArtist


class workerdownload(object):
    def __init__(self, base_url):
         self.base_url = base_url

	
    def initialurl (self):
        url = self.base_url
        usock = urllib2.urlopen(url)                                  
        file_name = url.split('/')[-1]                                #Example : for given url "www.cs.berkeley.edu/~vazirani/algorithms/chap6.pdf" file_name will store "chap6.pdf"
        f = open(file_name, 'wb')                                     #opening file for write and that too in binary mode.
        file_size = int(usock.info().getheaders("Content-Length")[0]) #getting size in bytes of file(pdf,mp3...)
        print "Downloading: %s Bytes: %s" % (file_name, file_size)
        downloaded = 0
        block_size = 8192
        while True:
            buff = usock.read(block_size)
            if not buff:
               break
        downloaded = downloaded + len(buff)
        f.write(buff)
        download_status = r"%3.2f%%" % (downloaded * 100.00 / file_size) #Simple mathematics
        download_status = download_status + (len(download_status)+1) * chr(8)
        print download_status,"done"
        f.close() 


if __name__ == '__main__':
    download = workerdownload('http://cdn-preview-9.deezer.com/stream/90353ef321c98df2c9135dd5a6870a18-2.mp3')
    listofSong = topSongArtist.objects.values()
    download.initialurl()
