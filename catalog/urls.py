from django.conf.urls import url
from .views import CategoryView, ProductView


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', CategoryView.as_view(), name='category_url'),
    url(r'^(?P<category__pk>\d+)/(?P<pk>\d+)/$', ProductView.as_view(), name='product_url'),
]
