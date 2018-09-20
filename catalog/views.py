from django.views import generic
from django.db.models import Count

from .models import Category, Product


class CategoryView(generic.DetailView):
    model = Category
    template_name = 'catalog/catalog_list.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['title'] = context['category'].title
        context['breadcrumbs'] = context['category'].get_breadcrumbs()
        context['categories'] = Category.objects.all()
        return context


class ProductView(generic.DetailView):
    model = Product
    template_name = 'catalog/catalog_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['title'] = context['product'].title
        context['breadcrumbs'] = context['product'].get_breadcrumbs()
        context['category'] = context['product'].category
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        queryset = super(ProductView, self).get_queryset()
        queryset = queryset.annotate(comments_count=Count('comments__id'))
        return queryset
