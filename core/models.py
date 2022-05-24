import os

from django.conf import settings
from django.db import models
from django.dispatch import receiver


class Image(models.Model):
    image = models.ImageField(upload_to=''.join(filter(str.isalnum, settings.MEDIA_URL)))
    generated_url = models.CharField(max_length=250, default='')

    def __repr__(self):
        return self.image.name


class Plan(models.Model):
    name = models.CharField(max_length=100)
    allow_height = models.IntegerField(null=False)
    originally_uploaded_file = models.BooleanField()
    expiring_link = models.IntegerField(null=True)


@receiver(models.signals.post_delete, sender=Image)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Image` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
