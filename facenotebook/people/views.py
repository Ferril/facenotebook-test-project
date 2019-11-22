from django.shortcuts import render
# from django.utils.safestring import mark_safe
from .redis_db import add_person, search_person
from .helpers import get_data_from_request, handle_uploaded_image


def add_person_view(request):
    template_name = 'add_person_form.html'
    if request.method == 'POST':
        request_data = request.POST.copy()
        photo = request.FILES.get('photo')
        person_photo = handle_uploaded_image(photo) if photo else b''
        data = {
            'surname': request_data['surname'],
            'name': request_data['name'],
            'patronymic': request_data['patronymic'],
            'photo': person_photo
        }
        add_person(data)
    return render(request, template_name)


def search_person_view(request):
    template_name = 'search_person_form.html'
    if request.method == 'GET':
        request_data = request.GET.copy()
        if request_data.get('action') == 'search':
            data_search = get_data_from_request(request_data)
            persons = search_person(data_search)
            return render(request, template_name, {'persons': persons})
    return render(request, template_name)
