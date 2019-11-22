from django.conf import settings
import uuid


def get_data_from_request(request_data):
    data = {
        b'surname': str.encode(request_data.get('surname', '')),
        b'name': str.encode(request_data.get('name', '')),
        b'patronymic': str.encode(request_data.get('patronymic', '')),
    }
    data_search = {}
    for key in data:
        if data[key]:
            data_search[key] = data[key]
    return data_search


def handle_uploaded_image(image):
    image_dir = '{}/images/{}.jpg'.format(settings.BASE_DIR, uuid.uuid4())
    with open(image_dir, 'wb+') as destination:
        for chunk in image.chunks():
            destination.write(chunk)
    image_url = 'file:/{}'.format(image_dir)
    return image_url
