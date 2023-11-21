from django.shortcuts import render, get_object_or_404, redirect
from .models import Posts
from rest_framework import generics, permissions, status, mixins
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .serializers import PostSerializer
from .forms import *
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.views import LoginView



def index(request):
    context = {
        'title': 'Migration Assistant',
        'post': Posts.objects.all(),
    }
    return render(request, 'general/index.html', context)

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'general/about.html', context)

def gallery(request):
    context = {
        'title': 'Gallery'
    }
    return render(request, 'general/gallery.html', context)

def contact(request):
    context = {
        'title': 'Contact'
    }
    return render(request, 'general/contact.html', context)

@csrf_protect
def single_post(request, post_slug):
    post = get_object_or_404(Posts, slug=post_slug)
    
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user.username
            new_comment.post = post
            new_comment.save()
        else:
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    
    data = {
        'post': post,
        'comment': post.comments.all(),
    }
    return render(request, 'general/single-post.html', context=data)

class Editor(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAdminUser] 

class CreatePost(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAdminUser]

@csrf_protect  
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('index')
    else:
        user_form = UserRegistrationForm()
    
    return render(request, 'general/register.html', {'reg_form': user_form})

def loggout(request):
    logout(request)
    return redirect('index')

