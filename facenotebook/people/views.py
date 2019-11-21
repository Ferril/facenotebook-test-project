from django.http import HttpResponseRedirect
from django.shortcuts import render


def add_person_view(request):
    template_name = 'add_person_form.html'
    if request.method == 'POST':
        # return HttpResponseRedirect('/thanks/')
        pass
    return render(request, template_name)


def search_person_view(request):
    template_name = 'search_person_form.html'
    return render(request, template_name)
