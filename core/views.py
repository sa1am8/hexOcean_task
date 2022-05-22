from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Image
from .serializers import ImageSerializer


def index(request):
    return Response('<h1> check')


class ImagesApi(APIView):
    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #serializer.create(validated_data=request.data)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
