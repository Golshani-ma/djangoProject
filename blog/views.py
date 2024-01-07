import datetime

from django.http import Http404
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def check_change_status(posts: Post):
    '''
        set the status of to 1.
    :param posts: The posts whose time has come to publish, but their status is zero
    :return: the posts that pub_date is lte than datetime.now()
    '''
    for p in posts:
        if p.status == 0:
            p.status = 1
            p.save()
    return None


# Create your views here.
def blog_view(request, cat_name=None, author_username=None):
    current_datetime = datetime.datetime.now()
    posts = Post.objects.filter(published_date__lte=current_datetime)
    # ************change status to 1 if pub_date<= now() **********************
    check_change_status(posts)

    posts = Post.objects.filter(status=1)

    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if author_username:
        posts = posts.filter(author__username=author_username)
    try:
        posts = Paginator(posts, 3)
        page_number = request.GET.get("page")
        posts = posts.get_page(page_number)


    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(posts.num_pages)

    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


# Create your views here.
def blog_single(request, pid):
    try:
        post = get_object_or_404(Post, id=pid, status=1)
        post.counted_views += 1
        post.save()
        context = {'post': post}
        return render(request, 'blog/blog-single.html', context)
    except Post.DoesNotExist:
        raise Http404("No MyModel matches the given query.")


def blog_category(request, cat_name):
    posts = Post.objects.filter(category__name=cat_name)
    # posts = posts.filter(category__name=cat_name)

    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_search(request):
    posts = Post.objects.filter(status=1)

    if request.method == 'GET':
        if s := request.GET.get('s'):
            print()
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def test(request):
    return render(request, 'test.html')
