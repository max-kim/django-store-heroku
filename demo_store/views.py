from django.shortcuts import HttpResponseRedirect
from django.http import HttpResponseNotFound, HttpResponse
from catalog.models import Category


def index_view(request):
    return HttpResponse('Hello world')
    # category = Category.objects.order_by('id').first()
    # if category:
    #     return HttpResponseRedirect(category.get_absolute_url())
    # else:
    #     return HttpResponseRedirect('www.google.com')
    #     # return HttpResponseNotFound('404 - PAGE NOT FOUND :(')
