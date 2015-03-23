from django import forms
from bucketlist.models import UserProfile, BucketListItems
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    location = forms.CharField(help_text="Please enter your location.", required=False)
    facebook = forms.URLField(help_text="Please enter your facebook.", required=False)
    
    class Meta:
        model = UserProfile
        fields = ('location', 'facebook')
        
class BucketListItemsForm(forms.ModelForm):
    
    
    class Meta:
        model = BucketListItems
        fields = ('title', 'description',  'finished', 'created', )
