from django.urls import path
from .api.apiviews import PersonView
from .views import add_person_view, search_person_view

urlpatterns = [
    path('add_person/', add_person_view, name='add_person'),
    path('find_person/', search_person_view, name='find_person'),
    path('api/', PersonView.as_view(), name='person_api')
]
