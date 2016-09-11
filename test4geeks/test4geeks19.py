class Human(object):

	def __setattr__(self, name, value):
		if name == 'gender':
			if value in ['maile', 'female']:
				self.gender = value
			else:
				raise AttributeError("Gender can only be maile or female")
				
h = Human()
h.name = "Mary"
h.gender = "female"

print(h.gender)

#line 6: self.gender = value !
#    if name == 'gender':
#RuntimeError: maximum recursion depth exceeded in comparison