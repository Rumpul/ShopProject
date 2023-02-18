from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.cart_detail, name='cart_detail'),
    re_path(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    re_path(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
    re_path(r'^quick_add/(?P<product_id>\d+)/$', views.one_click_cart_add, name='one_click_cart_add'),
]
