from django.conf.urls import url

from .views import index, feed, create_post, like, add_comment


urlpatterns = [
    url(r'^$', index),
    url(r'^post$', create_post, name='create_post'),
    url(r'^feed$', feed, name='feed'),
    url(r'^like/(?P<post_id>\d+)$', like, name='like'),
    url(r'^comment/(?P<post_id>\d+)$', add_comment, name='add_comment'),
]
