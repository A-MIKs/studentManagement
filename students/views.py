from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm
from django.contrib import messages


def index(request, deleted=False):
    students = Student.objects.all()
    return render(request, "students/index.html", {"students":students, "deleted":deleted})

def view_student(request, id):
  student = get_object_or_404(Student, pk=id) 
  return redirect("index")
    
def add(request):
    form = StudentForm()
    if request.method =="POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect("add")

    return render(request, "students/add.html", {
             "form": form,
          })

def edit(request, id):
    if request.method == "POST":
       student = get_object_or_404(Student, pk=id)
       form = StudentForm(request.POST, instance=student)
       if form.is_valid():
        form.save()
        messages.success(request, f"{student.first_name} updated successfully!")
        return redirect("index")
    student = get_object_or_404(Student, pk=id)
    form = StudentForm(instance=student)
    return render(request, "students/edit.html", {
             "form": form,
          })

def delete(request, id):
   if request.method == "POST":
      student = get_object_or_404(Student, pk=id)
      student.delete()
      messages.success(request, "Student deleted successfully!")
      return redirect("index")