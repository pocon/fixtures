from fixtures.models import *
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import Context, loader, RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def manage(request):
    return render_to_response('fixtures/manage.html')