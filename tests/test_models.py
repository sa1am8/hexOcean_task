import os

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from core.models import Image
from core.utils import generate_url

FILE_PATH = 'tests/media/mikkelsen.jpg'
FILE_NAME = 'mikkelsen.jpg'
TEST_NAME = 'test' + FILE_NAME


class DjangoModelsTestClass(TestCase):

    def setUp(self):
        image = Image(generated_url=generate_url(TEST_NAME))
        image.image = SimpleUploadedFile(name=TEST_NAME, content=open(FILE_PATH, 'rb').read(),
                                         content_type='image/jpeg')
        image.save()

    #def test_file_saved(self):
    #    self.assertTrue(os.path.isfile(TEST_NAME))

    def test_file_deleted_when_object_is_deleted(self):
        image_object = Image.objects.first()
        image_object.delete()
        self.assertFalse(os.path.isfile(TEST_NAME))
