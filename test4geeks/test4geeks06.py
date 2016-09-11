from datetime import datetime
from test4geeks06_constants import DEFAULT_DATE_FORMAT

def datefmt(date_string):
	return datetime.strptime(date_string, DEFAULT_DATE_FORMAT)

s = Student("Mary", "1981-7-23")


#ImportError: cannot import name 'DEFAULT_DATE_FORMAT'