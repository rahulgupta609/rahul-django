from __future__ import unicode_literals, absolute_import
from django.http.response import HttpResponse

def health_check(request):
    return HttpResponse("this is a test url to validate deployments", status=200)
