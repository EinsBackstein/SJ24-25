from django.db import models
from PIL import Image
import os
from django.conf import settings

class Department(models.Model):
    shortname = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.shortname + ' (' + self.description + ')'


class Person(models.Model):
    SEX_CHOICES = [('M','Male'), ('F', 'Female')]
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    sex = models.CharField(choices=SEX_CHOICES, max_length=1)
    description = models.TextField(blank=True)
    # Add this ImageField
    picture = models.ImageField(upload_to='person_pics/', null=True, blank=True)
    # The foreign key to the department model
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='people')

    
    # Get a thumbnail version of the picture
    def get_thumbnail(self):
        if self.picture:
            img = Image.open(self.picture.path)
            img.thumbnail((100, 100))

            thumbnail_filename = f'thumbnail_{os.path.basename(self.picture.name)}'
            thumbnail_dir = os.path.join('media', 'thumbnails')
            thumbnail_path = os.path.join(thumbnail_dir, thumbnail_filename)

            img.save(thumbnail_path)
            return os.path.join('/media', 'thumbnails', thumbnail_filename)
        return None
    
    def get_picturepath(self):
        if self.picture:
            return os.path.join('/media', self.picture.name)
        return None

    def __str__(self):
        return self.firstname + ' ' + self.lastname

    def delete(self, *args, **kwargs):
        # Delete the associated image file and thumbnail when the Person instance is deleted
        if self.picture:
            storage = self.picture.storage
            pic_path = self.picture.path
            thumbnail_filename = f'thumbnail_{os.path.basename(self.picture.name)}'
            thumbnail_path = os.path.join(settings.BASE_DIR, 'media', 'thumbnails', thumbnail_filename)
            super().delete(*args, **kwargs)
            storage.delete(pic_path)
            storage.delete(thumbnail_path)
        else:
            super().delete(*args, **kwargs)

