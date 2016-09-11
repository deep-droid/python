#https://pypi.python.org/pypi/Pafy

class BucketClass(object):
	bucketsize = 0
	water = 0
	def SizeOfBucket():
		print("Size: ", bucketsize)
		#return bucketsize
	
	def __init__(self, size):
		self.bucketsize = size
		
	def FillWater(self):
		water = bucketsize

	def GetSize(self):
		return self.bucketsize
	
	def GetWaterState(self):
		return self.water


class MyClass(object):
    field = 1

print (MyClass.field)


a = BucketClass(5)
b = BucketClass(3)

#a.SizeOfBucket
#b.SizeOfBucket

print ("status ", a.GetSize)
print ("status ", b.GetWaterState)

#b.PrintStatus

for element in [1, 2, 3]:
    #print(element)
	print("element",element)
	
	
#print("GetSize:", a.SizeOfBucket, "\n")
#print("GetSize:", b.getsize)

#print(.resolution, "n", s.extension, "\n", s.get_filesize(), "\n")

