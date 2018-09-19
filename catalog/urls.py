from django.urls import path
from .views import CategoryView, ProductView


urlpatterns = [
    path('<int:pk>/', CategoryView.as_view(), name='category_url'),
    path('<int:category>/<int:pk>/', ProductView.as_view(), name='product_url')
]
