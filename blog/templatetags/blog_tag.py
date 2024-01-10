from django import template
from blog.models import Post, Category
from django.utils import timezone

register = template.Library()


@register.simple_tag
def post_titles():
    posts = Post.objects.filter(status=1)
    return posts


@register.filter
def snippet_func(value, arg=20):
    return value[:arg] + '...'


@register.inclusion_tag('populerpost.html')
def popular_posts():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:2]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-lastposts.html')
def latest_post_side(num=4):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:num]
    return {'posts': posts}


@register.inclusion_tag('blog/post-categories.html')
def blog_post_categories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for cat_name in categories:
        cat_dict[cat_name.name] = posts.filter(category=cat_name).count()

    return {'categories': cat_dict}


@register.inclusion_tag('website/website-latest-posts.html')
def latest_post_bottom(num=6):
    '''
    Capter 7 Exersice Template Tag
    '''
    current_time = timezone.now()
    posts = Post.objects.filter(status=1, published_date__lte=current_time).order_by('-published_date')[:num]

    return {'posts': posts}
