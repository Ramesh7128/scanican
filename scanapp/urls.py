from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from scanapp.api.resources import DeviceResource, ProductsResource


v1_api = Api(api_name = 'v1')
v1_api.register(DeviceResource())
v1_api.register(ProductsResource())


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dailycheck.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(v1_api.urls)),
)
