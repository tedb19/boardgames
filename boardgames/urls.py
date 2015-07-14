from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# in the templates, or anywhere else, be sure to use the url name,
# and not the actual url, so that in future you have the flexibility to change
# the url mapping in only one place
urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.home', name='boardgames_home'),

)


# add patterns with the django.contrib.auth.views prefix
urlpatterns += patterns(
    'django.contrib.auth.views',

    url(r'^login/$', 'login',
        {'template_name': 'login.html'},
        name='boardgames_login'),

    url(r'^logout/$', 'logout',
        {'next_page': 'boardgames_home'},
        name='boardgames_logout'),
)
