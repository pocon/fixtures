from fixtures.models import *
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import Context, loader, RequestContext
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated():
        subs = Subscription.objects.filter(user=request.user)
        return render_to_response('fixtures/current.html', {'subs': subs,})
    else:
        return render_to_response('fixtures/index.html')

@login_required
def edit(request, sub_id):
    sub = get_object_or_404(Subscription, pk=sub_id)
    if sub.user == request.user:
        return render_to_response('fixtures/edit.html', {'sub': sub,})
    else:
        return render_to_response('fixtures/accessdenied.html')

@login_required
def new(request):
    return render_to_response('fixtures/new.html')