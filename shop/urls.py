from django.conf.urls import url
from shop.views import *


urlpatterns = [

    url(r'^$', ProductList, name='ProductList'),
    url(r'^(?P<category_slug>[-\w]+)/$', ProductList,   name='ProductListByCategory'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', ProductDetail, name='ProductDetail'),
]