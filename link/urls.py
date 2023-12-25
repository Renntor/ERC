from django.urls import path
from link.apps import LinkConfig
from link.views import LinkListCreateAPIView, LinkRetrieveUpdateDestroyAPIView

app_name = LinkConfig.name

urlpatterns = [
    path('', LinkListCreateAPIView.as_view(), name='list_crate_link'),
    path('<int:pk>/', LinkRetrieveUpdateDestroyAPIView.as_view(), name='retrieve_update_destroy_link')
]