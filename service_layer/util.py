 # -*- coding: utf-8 -*-


""" ©Prem Prakash
	General utility module 
"""

import os
import sys
import random
import pdb

import pickle
import logging
from bs4 import BeautifulSoup




#----------------------------------------------------------------------------

# Path to store and load data
K_PROJECT_DIR =  os.path.dirname(os.path.abspath(__file__)) # OLD: os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # os.path.dirname(os.getcwd())
# print('\n\n ****** K_PROJECT_DIR = {} ******'.format(K_PROJECT_DIR))
get_project_dir = lambda: K_PROJECT_DIR
msg = '[Project] dir = {}'.format(K_PROJECT_DIR)
get_results_dir = lambda arg='': os.path.join(get_project_dir(), 'results' , arg)

#Logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()
def reset_logger(filename='train_output.log'):
	logger.handlers = []
	filepath = os.path.join(get_results_dir(), filename)
	logger.addHandler(logging.FileHandler(filepath, 'w'))


def add_logger(filename):
	filepath = os.path.join(get_results_dir(), filename)
	logger.addHandler(logging.FileHandler(filepath, 'w'))


def setup_logger(filename='output.log'):
	filepath = os.path.join(get_results_dir(), filename)
	logger.addHandler(logging.FileHandler(filepath, 'a'))


#----------------------------------------------------------------------------

#Pickle py objects
class PickleHandler(object):    
	@staticmethod
	def dump_in_pickle(py_obj, filepath):
		"""Dumps the python object in pickle
			
			Parameters:
			-----------
				py_obj (object): the python object to be pickled.
				filepath (str): fullpath where object will be saved.
			
			Returns:
			--------
				None
		"""
		with open(filepath, 'wb') as pfile:
			pickle.dump(py_obj, pfile)
	
	
	
	@staticmethod
	def extract_from_pickle(filepath):
		"""Extracts python object from pickle
			
			Parameters:
			-----------
				filepath (str): fullpath where object is pickled
			
			Returns:
			--------
				py_obj (object): python object extracted from pickle
		"""
		with open(filepath, 'rb') as pfile:
			py_obj = pickle.load(pfile)
			return py_obj    


#----------------------------------------------------------------------------

#Better presentation of printed dict
import collections
def pretty(d, indent=0):
	""" Pretty printing of dictionary """
	ret_str = ''
	for key, value in d.items():

		if isinstance(value, collections.Mapping):
			ret_str = ret_str + '\n' + '\t' * indent + str(key) + '\n'
			ret_str = ret_str + pretty(value, indent + 1)
		else:
			ret_str = ret_str + '\n' + '\t' * indent + str(key) + '\t' * (indent + 1) + ' => ' + str(value) + '\n'

	return ret_str


def pretty_plain(d):

	for k, v in d.items():
		print(f'{{ key = {k}, value = {v} }}')



#----------------------------------------------------------------------------

# [How to use a dot “.” to access members of dictionary?] 
# (https://stackoverflow.com/questions/2352181/how-to-use-a-dot-to-access-members-of-dictionary)
class dotdict(dict):
	"""dot.notation access to dictionary attributes"""
	__getattr__ = dict.get
	__setattr__ = dict.__setitem__
	__delattr__ = dict.__delitem__


class DotDict(dict): 
	"""dot.notation access to dictionary attributes""" 
	def __getattr__(*args): 
		val = dict.get(*args) 
		return DotDict(val) if type(val) is dict else val
	
	__setattr__ = dict.__setitem__
	__delattr__ = dict.__delitem__


#----------------------------------------------------------------------------

if __name__ == '__main__':
	# pdb.set_trace()
	
	print('Util is the main module')

	nested_dict = {'val':'nested works too'}
	mydict = dotdict(nested_dict)
	print(mydict.val)


	d = {'foo': {'bar': 'baz'}}
	d = DotDict(d)
	print(d.foo.bar)