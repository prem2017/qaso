import json
import pdb

from django.shortcuts import render
from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt

from service_layer import main_entry


#----------------------------------------------------------------------------

def questions(request):
	print('\n\n\n***request = ', request)
	return render(request, 'sopage/questions.html') # HttpResponse('<h1> This is home page </h1>')


#----------------------------------------------------------------------------

# Create your views here.
def qac(request):
	print('\n[qac] request = ', request)

	out_json = {}
	try:
		search_text = request.GET.get('search_text', None)
		if not search_text:
			raise Exception('Missing parameters')
		print('search_text = ', search_text)
		out_json = main_entry.async_main_call(search_text)
		# pdb.set_trace()
		# print(out_json)
	except Exception as e:
		print("Exception  e = {0}".format(e))
		return HttpResponse(json.dumps( {"error": "Missing parameters", "status": 422 }), content_type = "application/json",  status=422)

	return HttpResponse(json.dumps(out_json), content_type = "application/json", status=200) 














