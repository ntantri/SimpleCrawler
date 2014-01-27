'''
	This class provides all custom exceptions that can occur
'''

class UsageError(Exception):
	'''This exception can be raised when there is an incorrect parameters are passed '''
	pass
	
class InvalidValue(ValueError):
	'''This error is called when the entered data by user is invalid'''
	pass	