class Bucket(object):
	def __init__(self, size):
		self.__size = 0
		self.__water = 0
		self.__size = size
		self.__water = 0

	def get_Size(self):
		return self.__size

	def set_Size(self, value):
		self.__size = value

	Size = property(fget=get_Size, fset=set_Size)

	def get_Water(self):
		return self.__water

	def set_Water(self, value):
		self.__water = value

	Water = property(fget=get_Water, fset=set_Water)

	def FillBucket(self):
		self.__water = self.Size

	def EmptyBucket(self):
		self.__water = 0

	def RemoveSomeWater(self, x):
		self.__water = self.Water - x

	def AddWater(self, bucket):
		temp = self.Size - self.Water
		if self.Water + bucket.Water <= self.Size:
			self.__water += bucket.Water
			bucket.EmptyBucket()
		else:
			self.__water += temp
			bucket.RemoveSomeWater(temp)

	def BucketStatus(self):
		Console.WriteLine("Size: {0} ; Water: {1}", self.Size, self.Water)

class Program(object):
	def Main(args):
		bucket5 = Bucket(5)
		bucket3 = Bucket(3)
		bucket3.FillBucket()
		bucket5.AddWater()
		bucket5.BucketStatus()
		bucket3.BucketStatus()
		bucket3.FillBucket()
		bucket5.BucketStatus()
		bucket3.BucketStatus()
		bucket5.AddWater()
		bucket5.BucketStatus()
		bucket3.BucketStatus()
		bucket5.EmptyBucket()
		bucket5.AddWater()
		bucket5.BucketStatus()
		bucket3.BucketStatus()
		bucket3.FillBucket()
		bucket5.AddWater()
		bucket5.BucketStatus()
		bucket3.BucketStatus()

	Main = staticmethod(Main)