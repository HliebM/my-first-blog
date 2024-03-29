from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm, UserCreateForm, LogInForm, CommentForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
def signUp(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'], email=form.cleaned_data['email'])
            user.save()
            return redirect(signIn)
    else:
        form = UserCreateForm()
    return render(request, 'blog/signUp.html', {'form': form})
def signIn(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                return redirect(post_list)
            else:
                form = LogInForm()
        else:
            #form = LogInForm()
            return redirect(post_list)
    else:
        form = LogInForm()
    return render(request, 'blog/signIn.html', {'form': form})
def post_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect(post_detail, pk=post.pk)
    else:
        form = CommentForm(instance=post)
    return render(request, 'blog/post_comment.html', {'form': form})
def post_delete(request, pk):
    get_object_or_404(Post, pk=pk).delete()
    return redirect(post_list)
def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.likes == 0:
        post.likes = 1
    else:
        post.likes = 0
    post.save()
    return redirect(post_list)
def post_like_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.likes == 0:
        post.likes = 1
    else:
        post.likes = 0
    post.save()
    return redirect(post_detail, pk=post.pk)







