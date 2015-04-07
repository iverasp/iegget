from django.db import models
from os import path
import shortuuid
import mimetypes
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from os import remove
from django.conf import settings

def file_cleanup(sender, instance, *args, **kwargs):
    remove(settings.UPLOAD_PATH + instance.filename)

class File(models.Model):

    file = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    uuid = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    filetype = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=255)
    size = models.FloatField(default=0)


    @classmethod
    def create(cls, title, filename):
        return cls(
            file=title,
            filename=filename,
            uuid=generate_uuid(),
            filetype=find_filetype(title),
            mimetype=mimetypes.guess_type(title),
            size=42,
        )

    def __str__(self):
        #return "<File: " + str(self.file) + ", UUID: " + str(self.uuid) + ">"
        return str(self.file)

#    @receiver(pre_delete, sender=File)
#    def delete_file(sender, instance, **kwargs):
#        remove(settings.UPLOAD_PATH + instance.filename)

pre_delete.connect(file_cleanup, sender=File)

def generate_uuid():
    return shortuuid.uuid()

def find_filetype(filename):
    name, file_ext = path.splitext(filename)
    return file_ext.split('.')[1]
