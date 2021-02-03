from django.shortcuts import render
from django.views import View


class ReviewView(View):
    reviews = ["Best book!", "Nice", "Good"]

    def get(self, request, *args, **kwargs):
        return render(request, 'book/reviews.html', context={'reviews': ReviewView.reviews})