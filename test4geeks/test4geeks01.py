with expression [as var]
	#...BODY...

#object is the result of the expression and must have __enter__ and __exit__ methods
#result of the expression must be context manager - implements context management protocol

#https://www.python.org/dev/peps/pep-0343/
# This PEP adds a new statement "with" to the Python language to make
# it possible to factor out standard uses of try/finally statements.

# In this PEP, context managers provide __enter__() and __exit__()
# methods that are invoked on entry to and exit from the body of the
# with statement.