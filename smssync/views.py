from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET',])
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
							"uuid": "1234567890"
						}
					]
				}
			}
			return Response(payload, status=status.HTTP_200_OK)

