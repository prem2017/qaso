# -*- coding: utf-8 -*-

# Copyright © Prem Prakash
# Main entry into the project for command line or through web-service

__author__ = 'Prem Prakash'


import os
import sys
import sys
import argparse
import re
import pdb
import json

import re
from bs4 import BeautifulSoup
import requests


from .data_scrapper import QuAndAnsScrapper
from .qa_compilation import QACompilation

from . import util


#----------------------------------------------------------------------------

def extract_so_urls(query):
	"""
		Parameters:
		-----------
			query (str): Question to find answer for

		Returns:
		--------
			urls (list): list of SO urls from the google search result
	"""
	import re
	from bs4 import BeautifulSoup
	import requests

	if not query:
		return []

	search_url = 'https://google.com/search?q=site:stackoverflow.com+'

	query_search_url = search_url + '+'.join(query.split(' ')) 
	print(query_search_url)

	soup = BeautifulSoup(requests.get(query_search_url).text, 'html.parser')

	sel_anchors = soup.select('a')

	so_base_url = 'https://stackoverflow.com'
	so_urls = [] 

	regex_c = re.compile(r'/q.*/(\d+)')
	for anchor in sel_anchors:
		url = anchor.attrs['href']
		reg_groups = regex_c.search(url)
		if reg_groups:
			so_urls.append(so_base_url + reg_groups.group(0))


	return so_urls






#----------------------------------------------------------------------------
	
# Input is URL
def extract_rc_and_answer(url):
	answer = QuAndAnsScrapper.scrap_so_page(url)
	
	qac = QACompilation(answer)
	qad_dict = qac.get_json()
	# print(qad_dict)

	return qad_dict



#----------------------------------------------------------------------------

# Input is question string
def search_answer(question):
	""" Search the <qstring> on google specifically on SO and extract the urls from the search page to process. 
		Parameters:
		-----------
			question (str): The string of the questiong asked

		Returns:
		--------
			out (dict): Return is a dictionary for keys = {q_title, q_body, 'rc', 'ans_body', 'suggestest_answers'}
	"""

	so_urls = extract_so_urls(question)
	if not so_urls:
		return {'rc': None, 'answer': None}

	out = {}

	suggestest_answers = {}
	answer = None
	qa_compilation = None
	main_url = None
	for i, url in enumerate(so_urls):
		if answer is None:
			answer = QuAndAnsScrapper.scrap_so_page(url)
			main_url = url
			if not (answer.get('acc_ans_id') or answer.get('max_voted_ans_id')):
				answer = None
		else:
			temp_title = QuAndAnsScrapper.extract_only_title(url)
			if temp_title:
				suggestest_answers[url] = temp_title

	# TODO: remove duplicates
	# print('\n\n main_url = ', main_url)
	# print('\n\n[suggestest_answers] = ', suggestest_answers)
	suggestest_answers.pop(main_url, None)

	# pdb.set_trace()
	if answer is not None:
		answer['suggestest_answers'] = suggestest_answers


	qac = QACompilation(answer)
	qad_dict = qac.get_json() 
	# print(qad_dict)

	return qad_dict


#----------------------------------------------------------------------------

def get_arg_parser():
	description = 'Give suitable arg for question of analysis of StackOverflwo url'
	
	parser = argparse.ArgumentParser(description=description)

	parser.add_argument('-q', '--question', type=str, default='', help='Write your question to get answer', required=False)

	parser.add_argument('-u', '--url', type=str, default='', help='Give URL to a StackOverflow question for its analysis.', required=False)

	return parser


#----------------------------------------------------------------------------

def main():
	parser = get_arg_parser()
	args = parser.parse_args()

	if not (args.question or args.url):
		parser.error('No action requested, add -q (question) or -u (URL of SO page)')

	if not args.question: 
		if 'stackoverflow.com/q' not in args.url.lower():
			parser.error('No action requested, add -q (question) or -u (URL of SO page eg. stackoverflow.com/question/9)')



	question = args.question
	so_url = args.url

	if question:
		search_answer(question.strip())
	else:
		extract_rc_and_answer(so_url.strip())



#----------------------------------------------------------------------------

# For Django call 
def async_main_call(search_text):
	if 'stackoverflow.com/q' in search_text.lower():
		return extract_rc_and_answer(search_text)
	else:
		return search_answer(search_text)


#----------------------------------------------------------------------------

if __name__ == '__main__':
	print('Entry point')
	main()

