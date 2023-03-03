from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def task(request):
	if request.method == 'GET':
		task = request.GET.get('task')
		if task == 'send':
			payload = {
				"payload":{
					"task":"send",
					"secret": "123456789",
					"messages": [
						{
							"to": "+639366256107",
							"message": "sample message",
							"uuid": "1234567891"
						},
						{
							"to": "+639532750785",
							"message": "custom message",
							"uuid": "1234567891"
						}
					]
				}
			}
			return Response(payload, status=status.HTTP_200_OK)
	p = {
		"payload":{
			"success":True,
			"error": None
		}
	}
	return Response(p, status=status.HTTP_200_OK)

