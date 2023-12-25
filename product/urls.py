from product.apps import ProductConfig
from django.urls import path
from product.views import ProductRetrieveUpdateDestroyAPIView, ProductListCreateAPIView


app_name = ProductConfig.name

urlpatterns = [
    path('', ProductListCreateAPIView.as_view(), name='list_create_product'),
    path('<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='retrieve_update_destroy_product')
]
