from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static # New Import
from registration.backends.simple.views import RegistrationView


if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


class MyRegistrationView(RegistrationView):
    def get_success_url(self,request,user):
        return '/bucketlist/'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'final_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^bucketlist/', include('bucketlist.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),
)
