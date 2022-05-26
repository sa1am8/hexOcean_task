import os
import uuid


def generate_url(name: str):
    return '/api/media/' + str(uuid.uuid5(uuid.NAMESPACE_DNS, name)).replace('-', '')[7:]


def delete_file_on_delete_object(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
