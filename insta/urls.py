from django.conf.urls import url, include
from insta.views import PostLikeToggle, PostLikeAPIToggle
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 

# app_name = 'insta'

urlpatterns = [
    url('^$', views.home,name='Instaflex'),
    url(r'^signUp/$', views.signUp, name='signUp'),
    url(r'^what_profile/(?P<profile_id>\d+)', views.my_profile, name='profile'),
    url(r'^account/', include('django.contrib.auth.urls')),
    url(r'^profile/<username>/', views.profile, name='profile'),
    url(r'^user_profile/<username>/', views.user_profile, name='user_profile'),
    url(r'^post/<id>', views.post_comment, name='comment'),
    url(r'^post/<id>/like', PostLikeToggle.as_view(), name='liked'),
    url(r'^api/post/<id>/like', PostLikeAPIToggle.as_view(), name='liked-api'),
    url(r'^like', views.like_post, name='like_post'),
    url(r'^search/$', views.search_results, name='search_results'),
    url(r'^unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    url(r'^follow/<to_follow>', views.follow, name='follow')
  
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
