from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'etsy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'storefront.views.home', name='home'),
    url(r'^store/(?P<store_id>\d+)/$', 'storefront.views.store', name='store'),
    url(r'^favorites/$', 'storefront.views.user_favorites', name='user_favorites'),
    url(r'^new_item/$', 'storefront.views.new_item', name='new_item'),



)
