from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PostForm
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required



def post_list(request):
    post_list = Post.objects.filter(is_published=True)\
        .filter(published_date__lte=timezone.now())\
        .order_by('-published_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


@login_required()
def draft_list(request):
    post_list = Post.objects.filter(is_published=False)\
        .order_by('-published_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'posts': posts}
    return render(request, 'blog/drafts.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)


@login_required()
def post_new(request):
    """
    There is no post_new template, it's just a view that sends you to the
    # post_edit template to enter a new post via a form
    """
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # this is redirecting you back to the post_detail view above
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'blog/post_edit.html', context)

@login_required()
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    context = {'form': form}
    return render(request, 'blog/post_edit.html', context)




