from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def task(request):
	if request.method == 'GET':
		task = request.GET.get('task')
		if task == 'send':
			payload = {
				"payload":{
					"task":"send",
					"secret_key": "123456789",
					"messages": [
						{
							"to": "+639975772141",
							"message": "sample message",
							"uuid": "123456789"
						}
					]
				}
			}
			return Response(payload, status=status.HTTP_200_OK)

