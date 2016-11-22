from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.index, name='index',),
    url(r'^create_quote$', views.create_quote, name='create_quote'),
    url(r'^show_user/(?P<id>\d+)$', views.show_user, name='show_user'),
    url(r'^add_fave/(?P<id>\d+)$', views.add_fave, name='add_fave'),
    url(r'^remove_quote/(?P<id>\d+)$', views.remove_quote, name='remove')
]

