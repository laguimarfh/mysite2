'''
index view project django
'''
from django.http import HttpResponse


def index(request):
    '''
    Index page with hello world response
    '''
    return HttpResponse('Hello world!')
