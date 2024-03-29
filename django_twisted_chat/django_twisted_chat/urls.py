from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_twisted_chat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^(/)?$', RedirectView.as_view(url='/chats/')),
    url(r'^chats/', include('chat.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

