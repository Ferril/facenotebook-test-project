from rest_framework import serializers


class PersonSerializer(serializers.Serializer):
    Surname = serializers.CharField(max_length=50, required=False)
    Name = serializers.CharField(max_length=50, required=False)
    Patronymic = serializers.CharField(max_length=50, required=False)
    Photo = serializers.ImageField()
