from django.urls import path 
from .views import ApiListView

urlpatterns = [
    path("liste_api", ApiListView.as_view(), name='liste'),
]
