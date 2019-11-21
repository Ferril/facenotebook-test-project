from django.urls import path
from .views import add_person_view, search_person_view

urlpatterns = [
    path('add_person/', add_person_view, name='add_person'),
    path('find_person/', search_person_view, name='find_person'),
]
