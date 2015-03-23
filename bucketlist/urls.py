from django.conf.urls import patterns, url
from bucketlist import views

urlpatterns = patterns('',
        url(r'^$', views.welcome, name='welcome'),
        url(r'about/$',views.about, name='about'),
        url(r'main/$',views.main, name='main'),
        url(r'toppicks/$',views.toppicks, name='toppicks'),
        url(r'yourlist/$',views.yourlist, name='yourlist'),
        url(r'profile/$', views.profile, name='profile'),
        url(r'profileedit/$', views.edit_profile, name='profileedit'),
        url(r'addlist/$', views.addlist, name='addlist'),
        #url(r'listedit/$',views.listedit, name='listedit'),
        )