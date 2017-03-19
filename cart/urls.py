from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$/cartAdd/(\d?)/$', CartAdd),
    url(r'^$', CartDetail, name='CartDetail'),
    url(r'^remove/(\d+)/$', CartRemove, name='CartRemove'),

]