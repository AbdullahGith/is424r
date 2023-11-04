from django.shortcuts import render, redirect
from .models import Student, Course
from .forms import StudentForm, CourseForm


def students(request):
    students_list = Student.objects.all()
    student_form = StudentForm(request.POST or None)

    if request.method == 'POST' and student_form.is_valid():
        student_form.save()
        return redirect('students')

    return render(request, 'myapp/students.html', {
        'students_list': students_list,
        'student_form': student_form
    })


def courses(request):
    courses_list = Course.objects.all()
    course_form = CourseForm(request.POST or None)

    if request.method == 'POST' and course_form.is_valid():
        course_form.save()
        return redirect('courses')

    return render(request, 'myapp/courses.html', {
        'courses_list': courses_list,
        'course_form': course_form
    })


def details(request, student_id):
    student = Student.objects.get(id=student_id)
    available_courses = Course.objects.exclude(students=student)

    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        if course_id:
            course = Course.objects.get(id=course_id)
            student.courses.add(course)

    return render(request, 'myapp/details.html', {
        'student': student,
        'available_courses': available_courses
    })