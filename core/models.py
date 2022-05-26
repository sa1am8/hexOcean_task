from django.db import models
from django.db.models.signals import post_delete

from .utils import delete_file_on_delete_object


class Image(models.Model):
    image = models.ImageField()
    generated_url = models.CharField(max_length=250, default='')

    def __repr__(self):
        return self.image.name

    def create(self, *args, **kwargs):
        super(Image, self).create(*args, **kwargs)


class Plan(models.Model):
    name = models.CharField(max_length=100)
    allow_height = models.IntegerField(null=False)
    originally_uploaded_file = models.BooleanField()
    expiring_link = models.IntegerField(null=True)


post_delete.connect(
    delete_file_on_delete_object, sender=Image, dispatch_uid="gallery.image.file_cleanup"
)
