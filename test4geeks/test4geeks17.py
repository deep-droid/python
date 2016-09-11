import copy
class A(object):
	pass
	
a = A()

a.lst = [1, 2, 3]
a.str = "cats and dogs"
b = copy.copy(a)

a.lst.append(100)
a.str = "cats and mice"

print (b.lst)
print (b.str)

#[1, 2, 3, 100]
#cats and dogs