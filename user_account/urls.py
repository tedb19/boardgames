from django.conf.urls import patterns, url


urlpatterns = patterns(
    'user_account.views',
    url(r'^home$', 'home', name='user_home'),
)
