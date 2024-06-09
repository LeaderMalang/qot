from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Services(models.Model):
    image = models.FileField(upload_to='images/')
    course_name = models.CharField(max_length=255)
    course_description = RichTextField()
    button_title = models.CharField(max_length=255)

    def __str__(self):
        return self.course_name

class Package(models.Model):
    price = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    features_lists = RichTextField()
    button_title = models.CharField(max_length=30)

class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name