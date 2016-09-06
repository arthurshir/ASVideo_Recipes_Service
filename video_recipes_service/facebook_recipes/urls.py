from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from facebook_recipes import views

urlpatterns = [
	url(r'^videos$', views.VideoList.as_view()),
	url(r'^pages$', views.FbPageList.as_view()),
	url(r'^pages/(?P<pageid>[\w\-]+)/$', views.FbPageDetail.as_view()),
	url(r'^pages/(?P<pageid>[\w\-]+)/videos$', views.FbPageVideoList.as_view()),
    url(r'^update/videos$', views.TriggerVideoFetch.as_view()),
    url(r'^update/pages$', views.TriggerFbPageFetch.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)