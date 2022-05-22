from rest_framework import serializers

from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, allow_empty_file=False)

    class Meta:
        model = Image
        fields = ['image']

    def create(self, validated_data):
        image = Image.objects.create(**validated_data)
        return image
