from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Student

from .forms import StudentForm, StudentSearchForm

def index(request):
    students = Student.objects.all()
    return render(request, 'students/index.html', {'students': students})

def view_student(request,id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))
    
def add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'students/add.html', {
                'form': StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()
    
    return render(request, 'students/add.html', {
        'form': form
    })
def edit(request,id):
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        form.save() 
        return render(request,'students/edit.html' ,{
            'form': form,
            'success': True
        })
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request,'students/edit.html',{
        'form': form
    })

def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))


def search(request):
    query = request.GET.get('query', '')
    if query:
        students = Student.objects.filter(first_name__icontains=query) | \
                   Student.objects.filter(last_name__icontains=query) | \
                   Student.objects.filter(email__icontains=query)
    else:
        students = Student.objects.all()
    
    return render(request, 'students/index.html', {'students': students, 'query': query})
