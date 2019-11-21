from rest_framework import views
from rest_framework.response import Response
from facenotebook.people.redis_db import search_person, add_person
from facenotebook.people.api.serializers import PersonSerializer
from facenotebook.people.helpers import get_data_from_request


class PersonView(views.APIView):

    def get(self, request):
        request_data = request.GET.copy()
        data_search = get_data_from_request(request_data)
        persons = search_person(data_search)
        results = PersonSerializer(persons, many=True).data
        return Response(results)

    def post(self, request):
        request_data = request.data.copy()
        data = {
            'surname': request_data.get('surname', ''),
            'name': request_data.get('name', ''),
            'patronymic': request_data.get('patronymic', ''),
            # 'photo': mark_safe(person_photo)
        }
        print(data)
        add_person(data)
        return Response(status=201)
