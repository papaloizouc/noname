from django.conf.urls import patterns, include, url
from django.contrib import admin
from noname.views import index


admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'noname.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
)
