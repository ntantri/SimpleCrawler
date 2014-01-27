'''
	This file creates the code to store the data structure
'''

class URLDataStore(object):
	def __init__(self):
		'''
			Initializes thr dict(hash) required for storing the tags
		'''
		self.url_dict = {}
		
	def add_url_data(self, key, value):
		'''
			Adds a new entry to the dict
		'''
		if key not in self.url_dict.keys():
			self.url_dict[key] = value
	
	def update_url_data(self, key, value):
		'''
			Updates the url value
		'''
		if key in self.url_dict.keys():
			self.url_dict[key] = value
			
	def last_added_url_value(self):
		'''
			Retrieves the last added value for the last key
		'''
		if self.url_dict.keys() > 0:
			return self.url_dict[self.url_dict.keys()[-1]]
			
	def last_added_url(self):
		'''
			Retrieves the last added url key
		'''
		return self.url_dict.keys()[-1]
	
	def delete_a_key(self, key):
		'''
			Deletes the specified key from the dict
		'''
		return self.url_dict.pop(key, None)
		
			