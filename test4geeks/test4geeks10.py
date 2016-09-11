class Organization(object):
	__employees = []
	
google = Organization()
google._Organization__employees.append("Erik")
google.__employees.append("Erik")

#AttributeError: 'Organization' object has no attribute '__employees' 