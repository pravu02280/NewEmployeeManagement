from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def testview(request):
    return HttpResponse(json.dumps({'name': 'Ajay'}), content_type='application/json')