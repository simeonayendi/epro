from django.shortcuts import render
from .models import Post, Comment
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import CommentForm


def post_list(request):
	posts = Post.objects.all()
	#is_liked = False
	#if posts.likes.filter(id=request.user.id).exists():
	#	is_liked = True
	context = {
		'posts':posts,
	#	'is_liked':is_liked,
	#	'total_likes': posts.total_likes(),
	}
	return render(request, 'blog/post_list.html', context)
#def like_post(request):
	posts = get_object_or_404(Post, id=request.POST.get('post_id'))
	#is_liked = False
	#if post.likes.filter(id=request.user.id).exists():
	#	post.likes.remove(request.user)
	#	is_liked = False
	#else:
	#	posts.likes.remove(request.user)
	#	is_liked = True
	#return HttpResponseRedirect(posts.get_absolute_url())

def post_detail(request, id, slug):
	post = get_object_or_404(Post, id = id, slug=slug)	
	posts = Post.objects.all()

	comments = Comment.objects.filter(Post=post).order_by('-id')

	if request.method == 'POST':
		comment_form = CommentForm(request.POST or None)
		if comment_form.is_valid():
			content = request.POST.get('content')
			comment = Comment.objects.create(Post=post, user=request.user, content=content)
			comment.save()
			return HttpResponseRedirect(post.get_absolute_url() )
	else:
		comment_form = CommentForm()



	context = {
		'post': post,
		'posts':posts,
		'comments':comments,
		'comment_form':comment_form,
	}
	return render(request, 'blog/post_detail.html', context)

