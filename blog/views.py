from django.views.generic import ListView, DetailView
from .models import Post, Seo_blog


# Create your views here.


class SeoBlogView:
    """Вывод SEO"""
    def get_seo_blog(self):
        return Seo_blog.objects.all()


class PostListView(SeoBlogView, ListView):
    """Страница со списком всех статей"""
    model = Post
    template_name = 'blog/blog_list.html'
    queryset = Post.objects.filter(published=True)


class PostDetailView(DetailView):
    """Страница со статьей"""
    model = Post
    slug_field = 'url'
    template_name = 'blog/blog_detail.html'
