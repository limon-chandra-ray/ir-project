from django.shortcuts import render
from django.http import JsonResponse
from .models import Region,Topic,Interview,Podcast
# Create your views here.
def topic_get(request):
    topic = Topic.objects.all().values("name",'slug')

    return JsonResponse({'status':'success','data':list(topic)},safe=False)
def region_get(request):
    region = Region.objects.all().values("name",'slug')

    return JsonResponse({'status':'success','data':list(region)},safe=False)
def interview_get(request):
    interview = Interview.objects.all().values("name",'slug')

    return JsonResponse({'status':'success','data':list(interview)},safe=False)
def podcast_get(request):
    podcast = Podcast.objects.all().values("name",'slug')

    return JsonResponse({'status':'success','data':list(podcast)},safe=False)
