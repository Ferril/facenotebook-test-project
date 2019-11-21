from django.http import HttpResponseRedirect
from django.shortcuts import render
from .redis_db import add_person, search_person


def add_person_view(request):
    template_name = 'add_person_form.html'
    if request.method == 'POST':
        request_data = request.POST.copy()
        photo = request.FILES.get('photo')
        person_photo = photo.read() if photo else ''
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
    if request.method == 'POST':
        request_data = request.POST.copy()
        print(request_data)
        data = {
            b'surname': str.encode(request_data['surname']),
            b'name': str.encode(request_data['name']),
            b'patronymic': str.encode(request_data['patronymic']),
        }
        data_search = {}
        for key in data:
            if data[key]:
                data_search[key] = data[key]
        search_person(data_search)
    return render(request, template_name)
