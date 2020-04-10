# -*- coding: utf-8 -*- 

# Copyright © Prem Prakash
# Scrapper module tests cases

__author__ = 'Prem Prakash'

import os
import pdb
import sys
import unittest

import requests
from bs4 import BeautifulSoup

from . import util
from .data_scrapper import QuAndAnsScrapper


#----------------------------------------------------------------------------

# Set up logger
logger = util.logger
if len(logger.handlers) <= 1:
	util.setup_logger()


#----------------------------------------------------------------------------

class TestQuAndAnsScrapper(unittest.TestCase):
	"""docstring for TestQuAndAnsScrapper"""
	def __init__(self, *args, **kwargs):
		super(TestQuAndAnsScrapper, self).__init__(*args, **kwargs)
		self.root_url = 'https://stackoverflow.com/questions/'


	def test_scrap_so_page(self):
		q_id = 37823770

		url = self.root_url + str(q_id)
		out = None
		try:
			out = QuAndAnsScrapper.scrap_so_page(url)
		except Exception as e:
			print(f'[Exception] = {e}')

		self.assertTrue(out is not None)
		self.assertTrue(out['q_title'] == 'Terraform stalls while trying to get IP addresses of multiple instances?')
		self.assertTrue(out['acc_ans_id'] == '37866044')
		self.assertTrue(out['max_voted_ans_id'] == '37866044')


#----------------------------------------------------------------------------

if __name__ == '__main__':
	unittest.main()
	print('********[Test Completed]********')
