from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Students

# List all students
def student_list(request):
    students = Students.objects.all()
    return render(request, 'students/index.html', {'students': students})

# Create a new student
def create_student(request):
    if request.method == 'POST':
        student = Students(
            student_id=request.POST.get('student_id'),
            name=request.POST.get('name'),
            which_class=request.POST.get('which_class'),
            age=request.POST.get('age')
        )
        student.save()
        return redirect(reverse('student_list'))
    
    return render(request, 'students/form.html', {'form_title': 'Add Student'})

# Edit a student
def edit_student(request, student_id):
    student = Students.objects.get(student_id=student_id)

    if request.method == 'POST':
        student.student_id = request.POST.get('student_id')
        student.name = request.POST.get('name')
        student.which_class = request.POST.get('which_class')
        student.age = request.POST.get('age')
        student.save()

        return redirect(reverse('student_list'))
    
    return render(request, 'students/form.html', {'form_title': 'Edit Student', 'student': student})

# Delete a student
def delete_student(request, student_id):
    student = Students.objects.get(student_id=student_id)
    student.delete()

    return redirect(reverse('student_list'))
