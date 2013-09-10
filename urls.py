from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hello.views.home', name='home'),
    # url(r'^hello/', include('hello.foo.urls')),
    (r'^index/$', 'hello.helloworld.index'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
   (r'^$','hello.list.index'), 
   (r'^list/$','hello.list.index'), 
   (r'^addcode/$','hello.result.addcode'), 
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
