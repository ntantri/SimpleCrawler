'''
	This is the helper class used for invoking html parser
'''
from html_parser import CrawlerHTMLParser
from cmdline_parser import CMDLineParser
from urlparse import urlparse
import urllib2

class CrawlHelper(object):
	
	@staticmethod		
	def validate_url_argument(args):
		'''
			This static method is used to validate the url entered by the user
			Takes a dict parameter that contains url key
		'''
		url = args.url
		op = urlparse(url)
		returnVal = ''
		if op.scheme is '' and op.netloc is '':
			returnVal = 'The url is not in correct format'
		else:
			try:
				if urllib2.urlopen(url).code / 100 >= 4:
					returnVal = 'The url is not accessible'
			except urllib2.URLError as e:
				returnVal = e
		return returnVal
		
	@staticmethod	
	def process_arguments():
		'''
			Invokes the command line parser for parsing the requested options
		'''
		cmdparser = CMDLineParser('Lets start the crawler')
		cmdparser.make_options('--url', help='Specify an url for starting the crawler')
		cmdparser.make_options('--interrupt', action='store_true', help='Specify whether the program should be stopped by an interrupt and via a fixed number')
		
		return cmdparser.parseOptions()
		
	@staticmethod
	def start_processing(values):
		'''
			Starts the parser/crawler that then processes the web contents
		'''
		starting_url = values['args'].url
		number_of_urls_to_fetch = None if not values['args'].interrupt else values['number_of_urls_to_fetch']
		crawler_parser = CrawlerHTMLParser()
		while True:
			parsed_values = crawler_parser.start_parsing(starting_url, number_of_urls_to_fetch)
			if parsed_values is None:
				break
			starting_url = parsed_values['starting_url']
			number_of_urls_to_fetch = parsed_values['num_of_urls_to_parse']