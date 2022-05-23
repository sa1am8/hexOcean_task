from rest_framework import status, renderers
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from hexOcean_task.settings import MEDIA_URL
from .models import Image
from .serializers import ImageSerializer


def index(request):
    return Response('<h1> check')


class JpegRenderer(renderers.BaseRenderer):  # also png renderer
    media_type = 'image/jpeg'
    format = 'jpeg'
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data


class ImagesApi(APIView):

    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        #request.data['url'] = request.data.get('image').name
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageResizeApi(APIView):
    renderer_classes = (JpegRenderer, JSONRenderer,)

    def get(self, request, image_name):
        image = Image.objects.filter(image=image_name)
        if image:
            image_file = open(MEDIA_URL + image_name, 'rb')
            return Response(data=image_file, status=status.HTTP_200_OK, content_type='image/jpeg')
        return Response(data={'error': 'true'}, status=status.HTTP_400_BAD_REQUEST)
