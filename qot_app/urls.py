from django.urls import path
from . import views

from django.contrib import admin

admin.site.site_header = 'QOT Adminsitration'                    # default: "Django Administration"
admin.site.index_title = 'QOT Adminsitration'                 # default: "Site administration"
admin.site.site_title = 'quranotarbiyah.com adminsitration' 
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('courses/', views.courses, name="courses"),
    path('packages/', views.packages, name="packages"),
]