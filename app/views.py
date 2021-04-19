from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *

def insert_topic(request):
    if request.method=='POST':
        topicname=request.POST['topic']
        t=Topic.objects.get_or_create(topic_name=topicname)[0]
        t.save()
        return HttpResponse('Data inserted SUccessfully')
    return render(request,'insert_topic.html')