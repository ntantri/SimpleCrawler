'''
	Simple crawler main code file
'''
import sys

from customexceptions import *
from helper import CrawlHelper
	
def get_input_for_limit():
	'''
		Gets the limit input that would have been set if user chooses to interrupt it with 
		a number that specifies the number of urls
	'''
	try:
		while True:
			number_of_urls = int(raw_input("Please enter the number of URLs to fetch (greater than 2)"))
			if number_of_urls < 2:
				print 'Invalid number. Should be greater than 2'
			else:				
				break				
	except ValueError:
		raise InvalidValue('Invalid integer number entered, please enter number grater than 2')
	return number_of_urls
	
def execute():
	'''
		Main method that initates the parsing of command arguments and 
		also invokes the helper which then starts the url crawl
	'''
	if len(sys.argv) < 2:
		raise UsageError('Incorrect usage. Provide --help to know more about it.')
	
	args = CrawlHelper.process_arguments()
	returnError = CrawlHelper.validate_url_argument(args)
	if returnError is '':
		values = { 'args': args }
	else:
		raise InvalidValue(returnError)
	
	if args.interrupt:
		number_of_urls_to_fetch = get_input_for_limit()
		values['number_of_urls_to_fetch'] = number_of_urls_to_fetch
			
	CrawlHelper.start_processing(values);

if __name__ == '__main__':
	execute()
	