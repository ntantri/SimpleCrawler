'''
	This code is responsible for parsing the html content
'''
from data_structure import URLDataStore
import urllib2
import re

class CrawlerHTMLParser(object):

	def __init__(self):
		'''
			Creates a url store that keeps track of all the url's
		'''
		self.url_store = URLDataStore()
	
	def start_parsing(self, starting_url, num_of_urls_to_parse):
		'''
			Queries the web and parses all the url's
		'''
		try:
			conn = urllib2.urlopen(starting_url)
			html = conn.read()
			urls = re.findall(r'href=[\'"]?([^\'" >]+)', html)
			self.url_store.add_url_data(starting_url, urls)
			print 'Starting crawler', starting_url
			for item in urls:
				if num_of_urls_to_parse is not None and  num_of_urls_to_parse > 1:
					num_of_urls_to_parse -= 1
					print item
				elif num_of_urls_to_parse is None:
					print item
				else:
					return
			self.url_store.update_url_data(starting_url, urls[1:])
			return { 'starting_url': urls[0], 'num_of_urls_to_parse': num_of_urls_to_parse}			
		except:
			self.url_store.delete_a_key(starting_url)
			last_added_url_value = self.perform_further_parsing()
			return { 'starting_url': last_added_url_value[0], 'num_of_urls_to_parse': num_of_urls_to_parse}			
			
	
	def perform_further_parsing(self):
		'''
			This method mainly consider's to remove and update the start of the next url
			for crawler
		'''
		last_added_url = self.url_store.last_added_url()
		last_added_url_value = self.url_store.last_added_url_value()
		if last_added_url_value is None:
			return
		else:
			if len(last_added_url_value) > 1:
				self.url_store.update_url_data(last_added_url, last_added_url_value[1:])
				return last_added_url_value[1:]
			else:
				perform_further_parsing()
				
				