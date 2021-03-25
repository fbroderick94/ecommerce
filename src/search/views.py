from django.shortcuts import render
from django.views.generic.list import ListView

from products.models import Product

# Create your views here.


class SearchProductView(ListView):
    template_name = 'search/view.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)
        else:
            return Product.objects.featured()
