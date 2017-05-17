from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^cart_adding/$', views.cart_adding, name='cart_adding'),

]


# urlpatterns = [
#
#     url(r'CartAdd/(\d+)/$', CartAdd, name='CartAdd'),
#     url(r'details/$', CartDetail, name='CartDetail'),
#     url(r'remove/(?P<product_id>\d+)/$', CartRemove, name='CartRemove'),
#
#     url(r'^$', CartDetail, name='CartDetail')
# ]