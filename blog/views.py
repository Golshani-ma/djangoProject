from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from blog.models import Post, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import timezone
from blog.forms import CommentForm


# Create your views here.
# @login_required(login_url='../accounts/login')
def blog_view(request, **kwargs):
    #  Chapter 6 - Part 1 Excersice
    current_datetime = timezone.now()
    posts = Post.objects.filter(status=1, published_date__lte=current_datetime).order_by('-published_date')

    if kwargs.get('cat_name') is not None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') is not None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') is not None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
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
    if request.method == 'POST':

        form = CommentForm(request.POST)
        # form.instance.post_id = pid
        print(form.instance.post_id)
        if form.is_valid():
            form.save()
            messages.success(request, 'کامنت  شما با موفقیت ثبت شد.')
        else:
            messages.error(request, 'متاسفانه کامنت شما ثبت نشد.')

    try:
        current_datetime = timezone.now()
        #  Chapter 6 - Part 1 Excersice
        post = get_object_or_404(Post, id=pid, status=1, published_date__lte=current_datetime)
        if request.method == 'GET':
            post.counted_views += 1
            post.save()

        #  Chapter 6-Part 2 Excersice
        lst_post = list(
            Post.objects.filter(status=1, published_date__lte=current_datetime).order_by('-published_date'))
        post_index = lst_post.index(post)
        if post_index > 0:
            prev_post = lst_post[post_index - 1]
        else:
            prev_post = None

        if post_index == len(lst_post) - 1:
            next_post = None
        else:
            next_post = lst_post[post_index + 1]
        if post.login_required:
            if request.user.is_authenticated:
                comments = Comment.objects.filter(post=post.id, approved=True).order_by('-create_date')
                form = CommentForm()
                context = {'post': post, 'prev_post': prev_post, 'next_post': next_post, 'comments': comments,
                           'form': form}
                return render(request, 'blog/blog-single.html', context)
            else:
                return HttpResponseRedirect(reverse('accounts:login'))
        else:
            comments = Comment.objects.filter(post=post.id, approved=True).order_by('-create_date')
            form = CommentForm()
            context = {'post': post, 'prev_post': prev_post, 'next_post': next_post, 'comments': comments,
                       'form': form}
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

# def test(request):
#     if request.method == 'POST':
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         subject=request.POST.get('subject')
#         message=request.POST.get('message')
#         print(name, email, subject, message)
#
#     return render(request, 'test.html')
