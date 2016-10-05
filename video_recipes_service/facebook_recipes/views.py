from fetch_facebook import fetchVideos, getFacebookPage
from facebook_recipes.models import Video, Facebook_Page
from facebook_recipes.serializers import VideoSerializer, FbPageSerializer
from rest_framework import mixins
from rest_framework import generics
import django_filters
from rest_framework import filters

# [buzzfeedtasty, buzzfeedpropertasty, MrCookingPanda, TabiEats, Tastemade, The Buddhist Chef]
# The Buddhist Chef refrenced from https://www.reddit.com/r/xxketo/comments/43lt33/buzzfeed_tasty_style_recipes/
pageList = ['1614251518827491', '1737181656494507', '126518947372806', '1443873339218987', '268804973206677', '1513229905659327']

# filters.LOOKUP_TYPES = ['gt', 'gte']

class VideoFilter(filters.FilterSet):
	created_ms__gt = django_filters.NumberFilter(name='created', lookup_expr='gt')
	class Meta:
		model = Video
		fields = {
			'created_ms': ['gt']
		}

class VideoList(generics.ListAPIView):
	serializer_class = VideoSerializer
	def get_queryset(self):
		"""
		This view should return a list of all the purchases for
		the user as determined by the username portion of the URL.
		"""
		queryset = Video.objects.all()
		created_ms_f = self.request.query_params.get('created_ms_f', None)
		if created_ms_f is not None:
			queryset = queryset.filter(created_ms__gte=created_ms_f)
		return queryset




class TriggerVideoFetch(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get(self, request, *args, **kwargs):
    	for page in pageList:
    		fetchVideos(page)
        return self.list(request, *args, **kwargs)

class FbPageList(generics.ListAPIView):
	queryset = Facebook_Page.objects.all()
	serializer_class = FbPageSerializer

class TriggerFbPageFetch(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Facebook_Page.objects.all()
    serializer_class = FbPageSerializer

    def get(self, request, *args, **kwargs):
    	for page in pageList:
    		getFacebookPage(page)
        return self.list(request, *args, **kwargs)

class FbPageDetail(generics.ListAPIView):
	def get_serializer_class(self):
		return FbPageSerializer

	def get_queryset(self):
		pageid = self.kwargs['pageid']
		return Facebook_Page.objects.filter(fbid=pageid)


class FbPageVideoList(generics.ListAPIView):
	def get_serializer_class(self):
		return VideoSerializer

	def get_queryset(self):
		pageid = self.kwargs['pageid']
		return Video.objects.filter(host_page__fbid = pageid)

