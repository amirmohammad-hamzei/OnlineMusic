from rest_framework import serializers


# Serializers define the API representation.
class SongSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    artist = serializers.CharField(max_length=200)