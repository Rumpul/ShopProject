from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^(?P<category_slug>[-\w]+)/$',
            views.reviews_list,
            name='reviews_list_by_category'),
    re_path(r'^stream/(?P<id>\d+)/$',
            views.get_streaming_video, name='stream'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
            views.review_detail,
            name='review_detail'),
    re_path(r'^$', views.reviews_list, name='reviews_list'),
]