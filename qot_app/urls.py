from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('courses/', views.courses, name="courses"),
    path('packages/', views.packages, name="packages"),
    path('blog/', views.blog, name="blog"),
    path('blog/<int:blog_id>/', views.blog_view, name='blog_view'),
    path('category/<int:category_id>/', views.blog_list_by_category, name='blog_list_by_category'),
    path('tag/<int:tag_id>/', views.blog_list_by_tags, name='blog_list_by_tags'),
    path('teacher_form/', views.teacher_form, name='teacher_form'),
    path('student_form/', views.student_form, name='student_form'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
]