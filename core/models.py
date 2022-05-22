from django.db import models
from django.conf import settings


# Create your models here.

class Image(models.Model):
    #id = models.IntegerField(primary_key=True, null=False, unique=True)

    image = models.ImageField(upload_to=''.join(filter(str.isalnum, settings.MEDIA_URL)))

    def __repr__(self):
        return self.image.name
