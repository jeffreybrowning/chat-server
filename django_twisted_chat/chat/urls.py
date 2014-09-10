from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_twisted_chat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name="index"),
    url(r'^(?P<chat_room_id>\S+)$', views.chat_room, name='chat_room')
)

