from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    location = models.CharField(max_length=128, blank=True, default='')
    facebook = models.URLField(blank=True, default='')
   # interests = 

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
       
def create_user_profile(sender, instance, created, **kwargs):  
      if created:  
         profile, created = UserProfile.objects.get_or_create(user=instance) 
         
post_save.connect(create_user_profile, sender=User) 

class BucketListItems(models.Model):
    user = models.ForeignKey(User, blank=True)
    title = models.CharField(max_length=128)
    finished = models.BooleanField(default=False)
    description = models.CharField(max_length=256)
    created = models.DateTimeField(default=timezone.now)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    
    
    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title

