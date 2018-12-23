from django.shortcuts import render
from blog.models import Post, Tag
from django.urls import reverse
from forum.models import Group, Category, Event
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def home(request):
	posts = Post.objects.all()[:13]
	group = Group.objects.filter()
	event = Event.objects.all()
	context = {
		'posts':posts,
		'group':group,
		'event':event,
	}
	return render(request, 'home/index.html', context)

