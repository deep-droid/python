#S1
#creates a list, elements stored in memory?
#elements generated when l.next() method is called?
l = [i for i in range(10000)]
#S2
#creates a generator function, elements stored in memeory
#elements generated when x.next() method is called?
x = (i for i in range(10000))

#list - memory
#generator - next()
