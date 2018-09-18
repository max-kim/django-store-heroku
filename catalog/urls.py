from django.urls import path
from .views import CategoryView, ProductView


urlpatterns = [
    path('<str:category_slug>/', CategoryView.as_view, name='category_url'),
    path('<str:category_slug>/<str:product_slug>/', ProductView.as_view, name='product_url')
]
