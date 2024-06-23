from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100)
    street_address = models.CharField(max_length=200)
    street_address_1 = models.CharField(max_length=200)
    country_of_residence = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    spouse_name = models.CharField(max_length=200, null=True, blank=True)
    from_which_country = models.CharField(max_length=200)
    education_experience = models.CharField(max_length=200)
    education_background = models.CharField(max_length=200)
    position_of_interest = models.CharField(max_length=200)
    hear_about = models.CharField(max_length=200)
    other_comments = models.CharField(max_length=200)

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

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100)
    street_address = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    academic_level = models.CharField(max_length=200)

    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    birth_date = models.CharField(max_length=100)

class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=300)
    cover_image = models.FileField(upload_to='images/')
    description = RichTextField()  # Assuming you're using a RichTextField for rich content
    category = models.ManyToManyField(Category, related_name='blogs')
    tag = models.ManyToManyField(Tag, related_name='blogs')

    def __str__(self):
        return self.title