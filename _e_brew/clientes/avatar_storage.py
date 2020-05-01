import os
import sys
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import FileSystemStorage


def avatar_path(instance, name):
    avatar_name = 'cli_id_' + str(instance.id) + '.' + name.rsplit('.', 1)[1]
    return os.path.join('avatares/', avatar_name)

MEDIUM = (400,400)
THUMBNAIL = (180,180)

class AvatarStorage(FileSystemStorage):

    def get_available_name(self, name, *args, **kwargs):
        """
        Remove de file if exists, and return the name for the save method.
        """
        self.delete(name)
        new = super().get_available_name(name, *args, **kwargs)
        return new

    def create_images(self, name, content):
        """
        Recibe a name and an image (content), and make the two sizes
        images for store them.
        """
        print('name es: ',name)
        print('content es :',content)

        im = Image.open(content)
        out_av = BytesIO()
        out_th = BytesIO()

        im.thumbnail(MEDIUM, Image.ANTIALIAS)
        im.save(out_av, format='JPEG', quality=100)
        out_av.seek(0)
        content_av = InMemoryUploadedFile(
            out_av,
            None, 
            "%s.jpg" % name.split('.')[0], 
            'image/jpeg', 
            sys.getsizeof(out_av),
            None
        )

        im.thumbnail(THUMBNAIL, Image.ANTIALIAS)
        im.save(out_th, format='JPEG', quality=100)
        out_th.seek(0)
        content_th = InMemoryUploadedFile(
            out_th,
            None, 
            "%s_th.jpg" % name.split('.')[0], 
            'image/jpeg', 
            sys.getsizeof(out_th),
            None
        )

        return content_av.name, content_av, content_th.name, content_th

    def save(self, name, content, max_length=None):
        """
        The original, code was commented, istead "create_images" method
        provide the name and content for avatar and thumbnail creation.
        """

        # if name is None:
        #     name = content.name

        # if not hasattr(content, 'chunks'):
        #     content = File(content, name)

        name = self.get_available_name(name, max_length=max_length)

        name_av, content_av, name_th, content_th = self.create_images(name, content)

        self._save(name_th, content_th)
        return self._save(name_av, content_av)
