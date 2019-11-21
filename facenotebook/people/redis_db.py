import uuid
from django.conf import settings
from redis import Redis


redis_data = Redis(**settings.REDIS_SETTINGS)


def add_person(data):
    key = str(uuid.uuid4())
    print(key)
    redis_data.hmset(key, data)


def search_person(data):
    search_result = set()
    keys = redis_data.keys()
    for id in keys:
        for key in data:
            bla = redis_data.hget(id, key)
            print(data[key], bla)
            if data[key] != bla:
                break
            search_result.add(id)
