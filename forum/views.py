from django.shortcuts import render
from .models import Group, Category, Event
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import PostCreateForm

def forum(request):
	group = Group.objects.filter()
	category = None
	#categories = Category.objects.filter(Group=Education)

	context = {
		'group':group,
		#'categories':categories,
		#'category':category,
	}

	return render(request, 'forum/home.html', context)
	
def forum_list(request,  slug):
	group = Group.objects.all()
	group = get_object_or_404(Group, slug=slug)
	context = {
		'group':group,
	}

	return render(request, 'forum/forum_list.html', context)

def group_create(request):
	if request.method == 'POST':
		form = PostCreateForm(request.POST or None)
		if form.is_valid():
			group = form.save(commit=False)
			group.author = request.user
			
			group.save()
			return redirect('forum:forum')
	else:
		form = PostCreateForm()
	context = {'form':form,}
	return render(request, 'forum/group_create.html', context)

def event(request):
	event = Event.objects.all()
	context = {}
	return render(request, 'events/event.html', context)




