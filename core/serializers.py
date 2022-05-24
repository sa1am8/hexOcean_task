from rest_framework import serializers

from .models import Image
from hexOcean_task.settings import MEDIA_URL


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, allow_empty_file=False)

    class Meta:
        model = Image
        fields = ['image', 'generated_url']

    def create(self, validated_data):
        image_object = Image.objects.create(**validated_data)
        image_object.image.name = image_object.image.name[len(MEDIA_URL):]
        image_object.save()
        return image_object
