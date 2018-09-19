from django.views import generic

from .models import Category, Product


class CategoryView(generic.DetailView):
    model = Category
    template_name = 'catalog/catalog_list.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['breadcrumbs'] = context['category'].get_breadcrumbs()
        context['categories'] = Category.objects.all()
        return context


class ProductView(generic.DetailView):
    model = Product
    template_name = 'catalog/catalog_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['breadcrumbs'] = context['product'].get_breadcrumbs()
        context['categories'] = Category.objects.all()
        return context
