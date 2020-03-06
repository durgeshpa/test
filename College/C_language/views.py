from django.shortcuts import render
from django.template import RequestContext
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
import time
# Create your views here.
def compile(request):
	import os

	if request.method=="POST":
		Run='timeout 5s ./a.out >outputs.txt'
		gcc='gcc'
		outputs='outputs.txt'
		data=request.POST.copy()
		code=(data.get('data'))
		print(code)
		file_name='main.c'
		file_in='input.txt'
		file_error='error.txt'
		commond=gcc +' '+file_name
		commond_error=commond+" 2> "+ file_error
		with open(file_name,'w+') as f:
			f.write(code)
			f.close()
		os.system(commond_error)
		error=None
		output=None
		with open(file_error) as f:
			error=f.readlines()
			f.close()

		time1=time.time()
		if(len(error)==0):
			output=os.system(Run)
			os.remove('a.out')
			
			#return render(request,'account/c.html',{'output':output})
			#print(output)
		elif os.path.isfile('a.out'):
			os.system(Run)
			error=None
			os.remove('a.out')
			
			
		else:
			print(error)
		#del output
		time2=time.time()
		executiontime=time2-time1
		if executiontime<4.5:
			if os.path.isfile(outputs):
				
				with open(outputs) as f:
					output=f.readlines()
					f.close()
				os.remove(outputs)
			
			os.remove(file_name)
			os.remove(file_error)
			
			#return render(request,'account/c.html',{'error':error,'output':output})
			print(output)
			return JsonResponse(json.dumps({'error':error,'output':output}),safe=False)
		else:
			
			os.remove(file_name)
			os.remove(file_error)
			print(error)

			#return render(request,'account/c.html',{'error':" execution time out",'output':None})
			return JsonResponse(json.dumps({'error':" execution time out"}),safe=False)
	else:
		return render(request,'account/c.html')
