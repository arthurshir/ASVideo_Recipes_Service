import facebook
import json
from datetime import timedelta, datetime
from django.utils.dateparse import parse_datetime
from facebook_recipes.models import Video, Facebook_Page


def fetchVideos(pageid):
	graph = facebook.GraphAPI(access_token='637343989764348|UIcj47P3UIq9EpbfOsHzd81Qln0', version='2.7')
	page = getFacebookPage(pageid)
	pageDict = graph.get_object(id=pageid, fields='videos.limit(100){id,picture,embed_html,created_time,description,permalink_url}')
	videoDictArray = pageDict['videos']['data']
	saveVideos(videoDictArray, page)

def getFacebookPage(pageid):
	graph = facebook.GraphAPI(access_token='637343989764348|UIcj47P3UIq9EpbfOsHzd81Qln0', version='2.7')
	pageDict = graph.get_object(id=pageid, fields='name,id,cover')
	page, _ = Facebook_Page.objects.get_or_create(fbid=pageDict['id'], name=pageDict['name'], image_url=pageDict['cover']['source'])
	page.save()
	return page



def saveVideos(videoDictArray, page):
	for videoDict in videoDictArray:
		saveVideo(videoDict, page)

def saveVideo(videoDict, page):
	# video, created = Video.objects.get_or_create(fbid=videoDict['id'])
	video = None
	try:
	    video = Video.objects.get(fbid=videoDict['id'])
	except Video.DoesNotExist:
		video = Video()
	video.created = parse_datetime(videoDict['created_time'])
	video.image_url = videoDict['picture']
	video.fbid = videoDict['id']
	video.page_url = "https://www.facebook.com" + videoDict['permalink_url']
	video.recipe_text = ''
	video.description = videoDict['description']
	video.host_page = page

	video.save()