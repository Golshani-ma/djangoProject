from django.http import Http404
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import timezone


# Create your views here.
def blog_view(request, cat_name=None, author_username=None):
    #  Chapter 6 - Part 1 Excersice
    current_datetime = timezone.now()
    posts = Post.objects.filter(status=1, published_date__lte=current_datetime).order_by('-published_date')

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
        #  Chapter 6 - Part 1 Excersice
        post.counted_views += 1
        post.save()

        #  Chapter 6 - Part 2 Excersice
        lst_post = list(Post.objects.filter(status=1).order_by('-published_date'))
        post_index = lst_post.index(post)
        if post_index > 0:
            prev_post = lst_post[post_index - 1]
        else:
            prev_post = None

        if post_index == len(lst_post) - 1:
            next_post = None
        else:
            next_post = lst_post[post_index + 1]

        context = {'post': post, 'prev_post': prev_post, 'next_post': next_post}
        return render(request, 'blog/blog-single.html', context)
    except Post.DoesNotExist:
        raise Http404("No MyModel matches the given query.")


def blog_category(request, cat_name):
    posts = Post.objects.filter(category__name=cat_name)

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
