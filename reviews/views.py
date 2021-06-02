
from django.views.generic.base import View
from django.shortcuts import render
from django.views.generic import ListView
from .models import Review, Seo_reviews
from .forms import ReviewForm

from django.contrib.auth.models import User
# Create your views here.


class SeoReviewView:
    """Получение SEO"""
    def get_seo_rev(self):
        return Seo_reviews.objects.all()




class ReviewListView(SeoReviewView, ListView):
    """Получение списка отзывов"""
    model = Review
    queryset = Review.objects.filter(published=True).order_by('-id')
    def get_context_data(self, **kwargs):
        context = super(ReviewListView, self).get_context_data(**kwargs)
        context['form'] = ReviewForm()
        return context

class AddReview(View):
    """Добавление отзыва через форму на сайте"""

    new_review = None

    def post(self, request):
        review_list = Review.objects.filter(published=True).order_by('-id')
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.author = request.user
            new_review.save()
        else:
            form = ReviewForm()
        return render(request, 'reviews/rev_was_added.html', {'new_review': new_review,
                                                          'review_list': review_list,
                                                          })