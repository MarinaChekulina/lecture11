from django.conf.urls import url

from .views import registration, login_view, logout_view, profile, users_list, subscribe, unsubscribe

urlpatterns = [
    url(r'^registration$', registration, name='registration'),

    url(r'^login$', login_view, name='login'),
    url(r'^logout$', logout_view, name='logout'),

    url(r'^list$', users_list, name='users'),

    url(r'^profile/(?P<username>[\w.+-]+)$', profile, name='profile'),
    url(r'^subscribe/(?P<user_id>\d+)$', subscribe, name='subscribe'),
    url(r'^unsubscribe/(?P<user_id>\d+)$', unsubscribe, name='unsubscribe'),
]