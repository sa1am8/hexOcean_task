import os

from django.conf import settings
from django.db import models
from django.dispatch import receiver


class Image(models.Model):
    image = models.ImageField(upload_to=''.join(filter(str.isalnum, settings.MEDIA_URL)))
    #url = models.CharField(max_length=200)

    def __repr__(self):
        return self.image.name


@receiver(models.signals.post_delete, sender=Image)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Image` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
