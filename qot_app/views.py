from django.shortcuts import render, redirect, get_object_or_404
from .models import Services, Contact, Package, Blog, Category, Tag, Teacher, Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        full_name = request.POST['fullName']
        mobile = request.POST['mobile']
        email = request.POST['email']
        country = request.POST['country']
        message = request.POST['message']
        contact = Contact(full_name=full_name, mobile=mobile, email=email, country=country, message=message)
        contact.save()
        return redirect('/contact/')
    return render(request, 'contact.html')

def courses(request):
    courses = Services.objects.all()
    return render(request, 'courses.html', {'courses':courses})

def packages(request):
    packages = Package.objects.all()
    return render(request, 'packages.html', {'packages':packages})

def blog(request):
    blogs = Blog.objects.all()
    side_blogs = Blog.objects.all()[:5]
    return render(request, 'blog.html', {'blogs':blogs, 'side_blogs':side_blogs})

def blog_view(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'single_blog.html', {'blog': blog})

def blog_list_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    blogs = category.blogs.all()
    side_blogs = Blog.objects.all()[:5]
    return render(request, 'blog_list_category.html', {'category': category, 'blogs': blogs, 'side_blogs':side_blogs})

def blog_list_by_tags(request, tag_id):
    tags = get_object_or_404(Tag, id=tag_id)
    blogs = tags.blogs.all()
    side_blogs = Blog.objects.all()[:5]
    return render(request, 'blog_list_tag.html', {'blogs': blogs, 'side_blogs':side_blogs})

def teacher_form(request):
    if request.method == 'POST':
        first_name = request.POST['teacher_first_name']
        last_name = request.POST['teacher_last_name']
        email = request.POST['teacher_email']
        password = request.POST['teacher_password']
        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=email, password=password)

        phone_number = request.POST['teacher_number']
        street_address = request.POST['teacher_street_address']
        street_address_1 = request.POST['teacher_address_line']
        country_of_residence = request.POST['teacher_country']
        city = request.POST['teacher_city']
        state = request.POST['teacher_state']
        postal_code = request.POST['teacher_zip']
        spouse_name = request.POST['teacher_spouse_name']
        from_which_country = request.POST['teacher_from_country']
        education_experience = request.POST['teacher_education_experience_select']
        education_background = request.POST['teacher_education_details']
        position_of_interest = request.POST['teacher_position_interest']
        hear_about = request.POST['teacher_hear_about']
        other_comments = request.POST['teacher_other_comments']

        teacher = Teacher(user=user, phone_number=phone_number, street_address=street_address, street_address_1=street_address_1, country_of_residence=country_of_residence, city=city, state=state, postal_code=postal_code, spouse_name=spouse_name, from_which_country=from_which_country, education_experience=education_experience, education_background=education_background, position_of_interest=position_of_interest, hear_about=hear_about, other_comments=other_comments)
        teacher.save()

        return redirect('/teacher_form/')
    return render(request, 'teacher_form.html')

def student_form(request):
    packages = Package.objects.all()
    if request.method == 'POST':
        email = request.POST['student_email']
        first_name = request.POST['student_first_name']
        last_name = request.POST['student_last_name']
        password = request.POST['student_password']

        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=email, password=password)

        package_price = request.POST['student_package']
        package = Package.objects.get(price=package_price)
        country = request.POST['student_country']
        street = request.POST['student_street']
        birth_date = request.POST['student_birthdate']
        city = request.POST['student_city']
        state = request.POST['student_state']
        postal_code = request.POST['student_postal_code']
        phone_number = request.POST['student_number']
        academic_level = request.POST['student_academic']

        student = Student(user=user, package=package, country=country, street_address= street, city=city, state=state, postal_code=postal_code, birth_date=birth_date, phone_number=phone_number, academic_level=academic_level)
        student.save()
        return redirect('/login/')
    
    return render(request, 'student_form.html', {'packages':packages})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('login_username')
        password = request.POST.get('login_password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/login/')
    else:
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('/')