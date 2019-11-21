def get_data_from_request(request_data):
    data = {
        b'surname': str.encode(request_data['surname']),
        b'name': str.encode(request_data['name']),
        b'patronymic': str.encode(request_data['patronymic']),
    }
    data_search = {}
    for key in data:
        if data[key]:
            data_search[key] = data[key]
    return data_search
