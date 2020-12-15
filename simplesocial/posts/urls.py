from django.conf.urls import url
from . import views

app_name = 'posts'
# to use in template tags

urlpatterns = [
    url(r'^$',views.PostList.as_view(),name='all'),
    url(r'new/$',views.CreatePost.as_view(),name='create'),
    url(r'by/(?P<username>[-\w]+)',views.UserPosts.as_views(),name='for_user'),
    url(r'by/(?P<username>[-\w]+)/(?P<pk>\d+)/$',views.PostDetail.as_views(),name='single'),
    url(r'delete/(?P<pk>\d+)/$',views.DeletePost.as_views(),name='delete'),
]


