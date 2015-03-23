from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,  HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from bucketlist.forms import UserForm, UserProfileForm, BucketListItemsForm
from bucketlist.models import BucketListItems, UserProfile
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
import datetime 
from django.utils import timezone
from django.db.models import Count





def main(request):
    return render(request, 'bucketlist/main.html')

def main(request):
     return render(request, 'bucketlist/yourlist.html')
     
  
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
 
@login_required 
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
        form = BucketListItemsForm(request.POST, instance=bucketlist)
        if form.is_valid():
            bucketlist = form.save(commit=False)
            bucketlist.user = request.user            
            print "checkin for errors" 
            #form.save()
            bucketlist.save()
            return redirect('yourlist')
        
        else:
            print errorrrr
    
    else:
        form = BucketListItemsForm(instance=bucketlist)
        
    return render(request, 'bucketlist/addlist.html', {'form': form, 'bucketlist': bucketlist})   
'''
@login_required 
def listedit(request):
    
    post = get_list_or_404(BucketListItems)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('blog.views.post_detail')
    else:
        form = BucketListItemsForm(instance=post)
    #return render(request, 'blog/post_edit.html', {'form': form})
    return render(request, 'bucketlist/listedit.html', {'form': form})
 
@login_required     
def listedit(request):
    user = request.user
    bucketlist = bucketlistitems.user
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        bucket_form = BucketListItemsForm(request.POST, instance=bucketlist)
        if bucket_form.is_valid:
            bucket_form.save()
            return redirect('profile')
        
        else:
            print profile_form.errors()
        
                                        
    else:
       user_form = UserForm(instance=user)
       bucket_form = BucketListItemsForm(instance=bucketlist)
        
    return render(request, 'bucketlist/listedit.html',
                       {'user_form': user_form, 'bucket_form': bucket_form}) 
'''   
def about(request):
    return render(request, 'bucketlist/about.html')

def welcome(request):
    return render(request, 'bucketlist/welcome.html')
    
def toppicks(request):

    bucket = BucketListItems.objects.values('title').annotate(c=Count('title')).order_by('-c')[:5]

    return render(request, 'bucketlist/toppicks.html', {'bucket': bucket})