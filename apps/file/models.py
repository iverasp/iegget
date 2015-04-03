from django.db import models
from os import path
import shortuuid
import mimetypes

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
        return "<File: " + str(self.file) + ", UUID: " + str(self.uuid) + ">"

def generate_uuid():
    return shortuuid.uuid()

def find_filetype(filename):
    name, file_ext = path.splitext(filename)
    print(name)
    return file_ext.split('.')[1]
