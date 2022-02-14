from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from FolloWUp.models import FollowUp

def myview(request):
    ...
    
# Create your views here.
def mark_attandance(request):
    html = "<html><body>It is now </body></html>"
    followup_id = request.GET.get('followup',0)
    attandance = request.GET.get('present',False) == "True"
    FollowUp.objects.filter(pk=followup_id).update(Present=attandance)
    parent = request.GET.get('parent','admin')
    return HttpResponseRedirect(parent)