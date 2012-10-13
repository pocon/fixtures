from fixtures.models import *
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import Context, loader, RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    if request.user.is_authenticated():
        subs = Subscription.objects.filter(user=request.user)
        return render_to_response('fixtures/current.html', {'subs': subs, 'messages': messages,})
    else:
        return render_to_response('fixtures/index.html', {'messages': messages,})

@login_required
def edit(request, sub_id):
    sub = get_object_or_404(Subscription, pk=sub_id)
    if sub.user == request.user:
        return render_to_response('fixtures/edit.html', {'sub': sub, 'messages': messages,})
    else:
        return render_to_response('fixtures/accessdenied.html', {'messages': messages,})

@login_required
def new(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        form.user = request.user
        if form.is_valid():
            return redirect('home')
    else:
        form = SubscriptionForm
    return render_to_response('fixtures/new.html', {'form': form, 'messages': messages,})
    # This form must be added into the template! Somebody go do that while I
    # get some cake!
    
@login_required
def delete(request, sub_id):
    sub = get_object_or_404(Subscription, pk=sub_id)
    if sub.user == request.user:
        messages.add_message(request, messages.INFO, 'Successfully Unsubscribed')
        # That is how to add a message ^^^
        # TODO: add in delete code here
        
