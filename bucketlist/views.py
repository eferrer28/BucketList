from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,  HttpResponseRedirect, QueryDict
from django.contrib.auth.decorators import login_required
from bucketlist.forms import UserForm, UserProfileForm, BucketListItemsForm
from bucketlist.models import BucketListItems, UserProfile
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
import datetime 
from django.utils import timezone
from django.db.models import Count
from django.contrib import messages



def main(request):
    return render(request, 'bucketlist/main.html')

     
  
@login_required    
def profile(request):
    user = request.user
    context_dict = {}
    try:
        user_profile = UserProfile.objects.get(user=user)
    except ObjectDoesNotExist:
        user_profile = {}

    return render(request, 'bucketlist/profile.html',
                  {'user': user, 'user_profile': user_profile})
    # return render(request, 'bucketlist/profile.html')
     
@login_required     
def edit_profile(request):
    user = request.user
    profile = user.userprofile
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, instance=profile)
        if profile_form.is_valid:
            profile_form.save()
            return redirect('profile')
        
        else:
            print profile_form.errors()
        
                                        
    else:
       user_form = UserForm(instance=user)
       profile_form = UserProfileForm(instance=profile)
        
    return render(request, 'bucketlist/profileedit.html',
                       {'user_form': user_form, 'profile_form': profile_form})
                

    
    #return render(request, 'bucketlist/profileedit.html', {'form': form})
"""
def yourlist(request): 
        if request.method == 'POST':
        # request.POST['content'] is a query string like 'entry[]=3&entry[]=2&entry[]=1'
        # convert to a QueryDict so we can do things with it
            entries = QueryDict(request.POST['content']) 
            for yourlist, list_pk in enumerate(request.POST.getlist('list[]')):
                print "is this thing on"
                list = get_object_or_404(BucketListItems, pk=int(str(list_pk)))
                list.order = yourlist
                list.save()
                return redirect('yourlist')

        
        return render(request, 'bucketlist/yourlist.html', {'list': list})

def yourlist(request):
    if request.method == 'POST':

        # request.POST['content'] is a query string like 'entry[]=3&entry[]=2&entry[]=1'
        # convert to a QueryDict so we can do things with it
        entries = QueryDict(request.POST['content'])

        for index, entry_id in enumerate(entries.getlist('entry[]')):
            # save index of entry_id as it's new order value
            print "fuck"
            entry = BucketListItems.objects.get(id=entry_id, user=user)
            entry.order = index
            entry.save()

    # split our entries arbitrarily, so we can have two lists on the page...
    entry_list1 = BucketListItems.objects.order_by('order')[:2]
    entry_list2 = BucketListItems.objects.order_by('order')[2:]


    return render(request, 'bucketlist/yourlist.html', {'entry_list1': entry_list1, 'entry_list2': entry_list2})   
"""
def yourlist(request):
    user = request.user
    context_dict = {}
    try:
        list = BucketListItems.objects.filter(user=user)
    except ObjectDoesNotExist:
        list = {}
    return render(request, 'bucketlist/yourlist.html', {'list': list, 'user':user})
   
    
@login_required    
def addlist(request):
    user = request.user
    id = request.GET.get('id', None)
    if id is not None:
        bucketlist = get_object_or_404(BucketListItems, id=id, user=user)
    
    else:
        bucketlist = None
            
    #user = request.user
    if request.method == 'POST':
        if request.POST.get('control') == 'delete':
            bucketlist.delete()
            messages.add_message(request, messages.INFO, 'Item Deleted!')
            return redirect('yourlist')

            
        form = BucketListItemsForm(request.POST, instance=bucketlist)
        if form.is_valid():
            bucketlist = form.save(commit=False)
            bucketlist.user = request.user            
            print "checkin for errors" 
            #form.save()
            bucketlist.save()
            return redirect('yourlist')
        
       
    
    else:
        form = BucketListItemsForm(instance=bucketlist)
        
    return render(request, 'bucketlist/addlist.html', {'form': form, 'bucketlist': bucketlist})   

def about(request):
    return render(request, 'bucketlist/about.html')

def welcome(request):
    return render(request, 'bucketlist/welcome.html')
    
def toppicks(request):

    bucket = BucketListItems.objects.values('title').annotate(c=Count('title')).order_by('-c')[:5]

    return render(request, 'bucketlist/toppicks.html', {'bucket': bucket})

"""    
def detail(request, entry_id):
    try:
        entry = Entry.objects.get(pk=entry_id)
    except Entry.DoesNotExist:
        raise Http404
    return render_to_response('entry/detail.html', {'entry': entry})
    
"""