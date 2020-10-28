from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# app_name = 'insta'

urlpatterns = [
    url(r'^$', views.feeds,name='feeds'),
    url(r'^registerPage/$', views.registerPage, name='registerPage'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^search/$', views.search_results, name='search_results'),
    url(r'^post/(\d+)',views.get_post_by_id,name ='post'),
    url(r'^story/', views.story, name='story'),
    url(r'^comment/(?P<pk>\d+)',views.comment,name='comment'),
    url(r'^like/(?P<operation>.+)/(?P<pk>\d+)',views.like, name='like'),
    url(r'^pillow/(?P<pk>\d+)', views.pillow, name='pillow'),
    url(r'^follow/(?P<operation>.+)/(?P<id>\d+)',views.follow,name='follow'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
