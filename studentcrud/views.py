from django.shortcuts import render, redirect

from django.contrib import messages

from studentcrud.forms import StudentForm
from studentcrud.models import Student

from django.http import HttpRequest, HttpResponse

# Create your views here.

def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})


def add_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully')
            return redirect('home')
    return render(request, 'add_student.html', {'form': form})


def student_details(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'student_details.html', {'student': student})

def update_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student details updated successfully')
            return redirect('home')
    form = StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form})

def delete_student(request, student_id):
    if request.method == 'POST':
        student = Student.objects.get(pk=student_id)
        student.delete()
        messages.success(request, 'Student has been deleted')
    return redirect('home')
