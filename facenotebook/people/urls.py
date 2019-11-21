from django.urls import path, include
from .views import add_person_view, search_person_view

urlpatterns = [
    path('add_person/', add_person_view),
    path('search/', search_person_view),
]
