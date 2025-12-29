from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Student
from .form import StudentForm

def index(request):
    return render(request, 'students/index.html', {
        'students': Student.objects.all()
    })

def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))


def _create_student_from_form(form):
    cd = form.cleaned_data
    return Student(
        student_number=cd['student_number'],
        first_name=cd['first_name'],
        last_name=cd['last_name'],
        email=cd['email'],
        field_of_study=cd['field_of_study'],
        gpa=cd['gpa'],
    )


def add(request):
    if request.method != 'POST':
        return render(request, 'students/add.html', {'form': StudentForm()})

    form = StudentForm(request.POST)
    if not form.is_valid():
        return render(request, 'students/add.html', {'form': StudentForm()})

    new_student = _create_student_from_form(form)
    new_student.save()
    return render(request, 'students/add.html', {
        'form': StudentForm(),
        'success': True
    })
    
def edit(request, id):
    student = Student.objects.get(pk=id)
    if request.method != 'POST':
        form = StudentForm(instance=student)
        return render(request, 'students/edit.html', {'form': form, 'student': student})

    form = StudentForm(request.POST, instance=student)
    if not form.is_valid():
        return render(request, 'students/edit.html', {'form': form, 'student': student})

    form.save()
    return render(request, 'students/edit.html', {
        'form': form,
        'student': student,
        'success': True
    })
    
    
    
def delete(request, id):
    student = get_object_or_404(pk=id)
    if request.method == "POST":
        student.delete()
        return redirect('index')
    return redirect('index')
