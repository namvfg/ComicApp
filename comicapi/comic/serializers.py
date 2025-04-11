from rest_framework import serializers
from comic.models import *

class ImageSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        req = super().to_representation(instance)
        req['image'] = instance.image.url
        return req

class ComicSerializer(ImageSerializer):
    class Meta:
        model = Comic
        fields = ['id', 'name', 'image', 'created_date', 'updated_date', 'status', 'view_count', 'description']






