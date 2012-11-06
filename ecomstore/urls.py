from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #(r'^$','preview.views.home'),
    (r'contact.html','preview.views.contact'),
    (r'about.html'  ,'preview.views.about'),
    (r'services.html','preview.views.services'),
    (r'index.html'    ,'preview.views.home'),
    (r'shop_online.html',include('ecomstore.catalog.urls')),
    # Examples:
    # url(r'^$', 'ecomstore.views.home', name='home'),
    # url(r'^ecomstore/', include('ecomstore.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
     (r'^cart/' , include('ecomstore.cart.urls')),
)
