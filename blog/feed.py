from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils import timezone

from blog.models import Post


class LatestEntriesFeed(Feed):
    title = "New Post"
    link = "/rss/feed"
    description = "New Post Rss Feed"

    def items(self):
        current_datetime = timezone.now()
        posts = Post.objects.filter(status=1, published_date__lte=current_datetime).order_by('-published_date')[:5]
        return posts

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:150]

    # item_link is only needed if NewsItem has no get_absolute_url method.
    # def item_link(self, item):
    #     return reverse("news-item", args=[item.pk])
