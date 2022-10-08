from django.urls import path
from .views import get_cluster

urlpatterns = [path('<cluster_id>', get_cluster)]
