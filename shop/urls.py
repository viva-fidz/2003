from django.conf.urls import url
from shop.views import *

urlpatterns = [

    url(r'category/$', CategoryList, name='CategoryList'),
    url(r'category/(\d+)', ProductList,   name='ProductList'),
    url(r'product/(\d+)', ProductDetail, name='ProductDetail'),
    url(r'^$/', ProductList, name='ProductList'),
]