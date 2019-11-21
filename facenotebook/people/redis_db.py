import uuid
from django.conf import settings
from redis import Redis


redis_data = Redis(**settings.REDIS_SETTINGS)


def add_person(data):
    key = str(uuid.uuid4())
    redis_data.hmset(key, data)


def search_person(data):
    search_result = []
    keys = redis_data.keys()
    for id in keys:
        flag = True
        person_data = redis_data.hgetall(id)
        for key in data:
            if data[key] != person_data[key]:
                flag = False
                break
        if flag:
            person = {
                "Surname": bytes.decode(person_data[b'surname']),
                "Name": bytes.decode(person_data[b'name']),
                "Patronymic": bytes.decode(person_data[b'patronymic'])
            }
            search_result.append(person)
        print(search_result)
    return search_result

