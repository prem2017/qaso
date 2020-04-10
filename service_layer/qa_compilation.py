# -*- coding: utf-8 -*-

# Copyright © Prem Prakash
# A class module to compile question, answers etc.

__author__ = 'Prem Prakash'


import sys
import pdb


#----------------------------------------------------------------------------

class QACompilation(object):
	"""docstring for QACompilation
	
	'q_title'
	'q_body': mainbar.select_one(qbody_idf),
	'q_id': mainbar.select_one(id_idf).attrs[id_idf_prop],
	'q_score': int(mainbar.select_one(vc_idf).attrs[vc_idf_prop])

	'parent_id': parent_id,
	'acc_ans_body': accepted_ans_body,
	'acc_ans_id': accepted_ans_id,
	'acc_ans_score': accepted_ans_score,
	'max_voted_ans_body': max_voted_ans_body,
	'max_voted_ans_id': max_voted_ans_id,
	'max_voted_ans_score': max_voted_ans_score

	'suggestest_answers' (list)

	"""
	def __init__(self, arg_dict):
		super(QACompilation, self).__init__()
		
		# pdb.set_trace()

		self.q_title = arg_dict['q_title']
		self.q_body = arg_dict['q_body']
		self.q_url = arg_dict['q_url']

		self.acc_ans_body = None
		self.most_voted_ans_body = None

		self.acc_ans_id = None
		self.most_voted_ans_id = None

		self.is_ans_accepted = False

		if arg_dict.get('acc_ans_body', None):
			self.acc_ans_body = arg_dict.get('acc_ans_body')
			self.is_ans_accepted = True
			self.acc_ans_id = arg_dict.get('acc_ans_id')

		self.most_voted_ans_body = arg_dict.get('max_voted_ans_body', None)
		self.max_voted_ans_id = arg_dict.get('max_voted_ans_id', None)


		self.suggestest_answers = []
		if arg_dict.get('suggestest_answers', None):
			# print("arg_dict.get('suggestest_answers') = \n", arg_dict.get('suggestest_answers'))
			self.set_suggestest_answers(arg_dict.get('suggestest_answers'))



	def set_suggestest_answers(self, suggestest_answers):
		if not suggestest_answers:
			return
		self.suggestest_answers = suggestest_answers
		


	def get_json(self):

		json_data = {'q_title': str(self.q_title),
			'q_url': self.q_url,
			'q_body': str(self.q_body),

			'is_ans_accepted': self.is_ans_accepted,

			'most_voted_ans_body': str(self.most_voted_ans_body),
			'acc_ans_body': str(self.acc_ans_body),

			'suggestest_answers': self.suggestest_answers
		}
		return json_data



















