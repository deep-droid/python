import pafy
#https://pypi.python.org/pypi/Pafy
video = pafy.new("http://www.youtube.com/watch?v=UpSiU_gPaJA")

streams = video.streams
for s in streams:
     print(s.resolution, "n", s.extension, "\n", s.get_filesize(), "\n")
	 #print(s.resolution, "n", s.extension, "\n", s.get_filesize(), "\n", s.url)
	 
best = video.getbest()
best.download(quiet=False)
