from django.shortcuts import render_to_response
from django.template.context import RequestContext

def form(request):
  return render_to_response('form.html', {},
      context_instance=RequestContext(request))
