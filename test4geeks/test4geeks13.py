class A:
	brothers =[]
	def __init__(self, name):
		self.name = name

a = A("Richard")
b = A("Elly")
a.brothers.append("John")

print(a.name, a.brothers, b.name, b.brothers)

#Richard ['John'] Elly ['John']
