# -*- coding: utf-8 -*- 

# Copyright © Prem Prakash
# Scrapper module to extract data from SO page

__author__ = 'Prem Prakash'


import os
import pdb
import sys
import time

import requests
from bs4 import BeautifulSoup

from . import util


#----------------------------------------------------------------------------

# Set up logger
logger = util.logger
if len(logger.handlers) <= 1:
	util.setup_logger()


#----------------------------------------------------------------------------

class QuAndAnsScrapper(object):
	""" Scraps pages fo stackoverflow
		DataFrame columns:
		id,Title,Body,AcceptedAnswerId,Score,AnswerCount,Tags,ViewCount
		Source: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#differences-between-parsers
	"""


	@staticmethod
	def extract_ques_title(soup):
		"""Extracts question title from the root soup of the page
			Parameters:
			-----------
				mainbar (bs4.element.Tag): the answer section of the page 

			Returns:
			--------
				Title of the question
		"""
		qtitle_idf = '#question-header .question-hyperlink'
		# pdb.set_trace()
		title_tag = soup.select_one(qtitle_idf)
		if title_tag:
			return title_tag.get_text()
		else:
			return None

	@staticmethod
	def extract_ques_body(mainbar):
		"""Extracts question body from the main section of the page
			Parameters:
			-----------
				mainbar (bs4.element.Tag): the answer section of the page 

			Returns:
			--------
		"""
		qbody_idf = '.question .post-text' 
		id_idf = '.question'
		id_idf_prop = 'data-questionid'
		
		vc_idf = '.js-vote-count' 
		vc_idf_prop = 'data-value'
		return {'q_body': mainbar.select_one(qbody_idf),
				'q_id': mainbar.select_one(id_idf).attrs[id_idf_prop],
				'q_score': int(mainbar.select_one(vc_idf).attrs[vc_idf_prop])
				}



	@staticmethod
	def extract_answers(mainbar, parent_id):
		""" Extracts accepted and most voted answer from the mainbar- which is id  answer section of the page

			Parameters:
			-----------
				mainbar (bs4.element.Tag): the answer section of the page 

			Returns:
			--------
				Dictionary of accepted answer info and most-voted answer

			# TODO: Replace hard-coded indentifiers
		"""
		ans_idf='.answer'  
		accepted_ans_idf='.accepted-answer'
		ans_body_idf = '.post-text'
		ans_id_idf_prop = 'data-answerid'

		vc_idf = '.js-vote-count' 
		vc_idf_prop = 'data-value'

		accepted_ans_body = None
		accepted_ans_id = None
		accepted_ans_score = None
		
		accepted_ans = mainbar.select_one(accepted_ans_idf) # 'accepted-answer' in max_voted_answer.attrs['class']
		if accepted_ans is not None:
			accepted_ans_body = accepted_ans.select_one(ans_body_idf)
			accepted_ans_id =  accepted_ans.get(ans_id_idf_prop)
			accepted_ans_score = int(accepted_ans.select_one(vc_idf).get(vc_idf_prop))
			


		max_voted_ans_body = None
		max_voted_ans_id = None
		max_voted_ans_score = None

		# pdb.set_trace()
		all_answers = mainbar.select(ans_idf)
		if all_answers is None:
			all_answers = []

		for ans in all_answers:
			# print(type(ans))

			score = int(ans.select_one(vc_idf).get(vc_idf_prop))
			# print(score)

			if max_voted_ans_score is None:
				max_voted_ans_score = score
				
			if score >= max_voted_ans_score:
				max_voted_ans_body = ans.select_one(ans_body_idf)
				max_voted_ans_id = ans.get(ans_id_idf_prop)
				max_voted_ans_score = score


		return {
			'parent_id': parent_id,
			'acc_ans_body': accepted_ans_body,
			'acc_ans_id': accepted_ans_id,
			'acc_ans_score': accepted_ans_score,
			'max_voted_ans_body': max_voted_ans_body,
			'max_voted_ans_id': max_voted_ans_id,
			'max_voted_ans_score': max_voted_ans_score
		}


		
	@staticmethod
	def get_html_soup(url):
		

		try:
			html = requests.get(url)
		except requests.exceptions.Timeout as e:
			# Maybe set up for a retry, or continue in a retry loop
			print(f'[requests.exceptions.Timeout] {e}')
			raise
		except requests.exceptions.RequestException as e:
			# catastrophic error. bail.
			print(f'[requests.exceptions.RequestException] {e}')
			raise
		except Exception as e:
			print(f'[Exception] There seem to be problem with URL = {url}\ne={e}')
			raise

		return BeautifulSoup(html.text, 'html.parser')	

	@staticmethod
	def scrap_so_page(url):
		"""Scrapes SO page for question and answer details 
			and resturns HTML text. Note that it is not post processed 
			to be in text form only.  

		"""		
		mainbar_idf = '#mainbar'

		soup =  QuAndAnsScrapper.get_html_soup(url)

		mainbar = soup.select_one(mainbar_idf)

		question_title = QuAndAnsScrapper.extract_ques_title(soup)
		question_body = QuAndAnsScrapper.extract_ques_body(mainbar)

		parent_id = question_body['q_id']
		answers_body = QuAndAnsScrapper.extract_answers(mainbar, parent_id)


		compiled_qa = {'q_title': question_title, 'q_url': url}
		compiled_qa = {**compiled_qa, **question_body, **answers_body}
		return compiled_qa


	@staticmethod
	def extract_only_title(url):
		soup = QuAndAnsScrapper.get_html_soup(url)

		return QuAndAnsScrapper.extract_ques_title(soup)


#----------------------------------------------------------------------------

if __name__ == '__main__':
	print('[Module] DataScrapper')

	print('Scrap Answers')







