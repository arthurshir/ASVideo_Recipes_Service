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

# class VideoFilter(filters.FilterSet):
#     timestamp_gte = django_filters.DateTimeFilter(name="created", lookup_expr='gte')
#     class Meta:
#         model = Video
#         fields = ['created', 'created_gte']

class VideoList(generics.ListAPIView):
	queryset = Video.objects.all()
	serializer_class = VideoSerializer
	# filter_class = VideoFilter
	filter_fields = ['created_ms']
	filter_backends = (filters.DjangoFilterBackend,)
    

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

