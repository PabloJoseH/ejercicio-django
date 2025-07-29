from django.urls import path
from .views import (
    CheeseListView, CheeseCreateView, CheeseDetailView,
    CheeseUpdateView, CheeseDeleteView, CheeseAddCustomView
)

app_name = "cheeses" 

urlpatterns = [
    path("",       CheeseListView.as_view(),   name="list"),
    path("add/",   CheeseCreateView.as_view(), name="add"),
    path("cheeses/add-custom/", CheeseAddCustomView.as_view(), name="cheese_add_custom"),
    path("<int:pk>/",       CheeseDetailView.as_view(),   name="detail"),
    path("<int:pk>/edit/",  CheeseUpdateView.as_view(),   name="update"),
    path("<int:pk>/delete/",CheeseDeleteView.as_view(),   name="delete"),
]
