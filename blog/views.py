from django.http import Http404
from django.shortcuts import render, get_object_or_404
from blog.models import Post


# Create your views here.
def blog_view(request, cat_name=None, author_username=None):
    posts = Post.objects.filter(status=1)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if author_username:
        posts = posts.filter(author__username=author_username)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


# Create your views here.
def blog_single(request, pid):
    try:
        post = get_object_or_404(Post, id=pid, status=1)
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
