
from django.shortcuts import render
from .forms import UserCreationForm, UserLoginForm
from home.views import home
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, get_user_model, logout
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home:home'))
    else:
        form = UserCreationForm()

    context = {'form':form}
    return render(request, 'accounts/register.html', context)

"""
def login_view(request, *args, **kwargs):
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		user_obj = form.cleaned_data.get('user_obj')
		login(request, user_obj)
		return HttpResponseRedirect("/")
	return render(request, "accounts/login.html", {"form":form})
"""
def logout_view(request):
	logout(request)
	return HttpResponseRedirect("/login")


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('blog:home'))
                else:
                    return HttpResponse("<h1>User is none</h1>")
    else:
        form = UserLoginForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

#@login_required
def profile(request):
    args = {'user':request.user}
    return render(request, 'accounts/profile.html', args)
