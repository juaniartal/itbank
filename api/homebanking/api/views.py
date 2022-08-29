from pickle import PERSID
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(requestt):
    person = {'name': 'Dennis'}
    return Response(person)