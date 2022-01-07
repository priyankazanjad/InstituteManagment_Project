from django.shortcuts import render,redirect
from .forms import DepartmentModelForm,ProfessorModelForm,StudentModelForm
from .models import Department,Professor,Student

def adddepartmentmodel(request):
    form = DepartmentModelForm()
    if request.method == 'POST':
        form = DepartmentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_dept')
    template_name = 'InstituteApp/adddepartment.html'
    context = {'form':form}
    return render(request,template_name,context)

def showdepartment(request):
    department = Department.objects.all()
    if request.method == 'POST':
        department = Department.objects.filter(dept_name__icontains=request.POST['searchdata'])
    context = {'department':department}
    template_name = 'InstituteApp/showdepartment.html'
    return render(request,template_name,context)

def deletedepartment(request,i):
    department = Department.objects.get(dept_name=i)
    if request.method == 'POST':
        department.delete()
        return redirect('show_dept')
    context = {'department':department}
    template_name = 'InstituteApp/deletedepartment.html'
    return render(request,template_name,context)

def updatedepartment(request,i):
    department = Department.objects.get(dept_name=i)
    form = DepartmentModelForm(instance=department)
    if request.method == 'POST':
        form = DepartmentModelForm(request.POST,instance=department)
        if form.is_valid():
            form.save()
            return redirect('show_dept')
    context = {'form':form}
    template_name = 'InstituteApp/adddepartment.html'
    return render(request,template_name,context)

def addprofessormodel(request):
    form = ProfessorModelForm()
    if request.method == 'POST':
        form = ProfessorModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_prof')
    template_name = 'InstituteApp/addprofessor.html'
    context = {'form':form}
    return render(request,template_name,context)

def showprofessor(request):
    professor = Professor.objects.all()
    if request.method == 'POST':
        professor = Professor.objects.filter(prof_name__icontains=request.POST['searchdata'])
    context = {'professor':professor}
    template_name = 'InstituteApp/showprofessor.html'
    return render(request,template_name,context)

def deleteprofessor(request,i):
    professor = Professor.objects.get(prof_name=i)
    if request.method == 'POST':
        professor.delete()
        return redirect('show_prof')
    context = {'professor':professor}
    template_name = 'InstituteApp/deleteprofessor.html'
    return render(request,template_name,context)

def updateprofessor(request,i):
    professor = Professor.objects.get(prof_name=i)
    form = ProfessorModelForm(instance=professor)
    if request.method == 'POST':
        form = ProfessorModelForm(request.POST,instance=professor)
        if form.is_valid():
            form.save()
            return redirect('show_prof')
    context = {'form':form}
    template_name = 'InstituteApp/addprofessor.html'
    return render(request,template_name,context)

def addstudentmodel(request):
    form = StudentModelForm()
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_stu')
    template_name = 'InstituteApp/addstudent.html'
    context = {'form':form}
    return render(request,template_name,context)

def showstudent(request):
    student = Student.objects.all()
    if request.method == 'POST':
        student = Student.objects.filter(name__icontains=request.POST['searchdata'])
    context = {'student':student}
    template_name = 'InstituteApp/showstudent.html'
    return render(request,template_name,context)

def deletestudent(request,i):
    student = Student.objects.get(rollno=i)
    if request.method == 'POST':
        student.delete()
        return redirect('show_stu')
    context = {'student':student}
    template_name = 'InstituteApp/deletestudent.html'
    return render(request,template_name,context)

def updatestudent(request,i):
    student = Student.objects.get(rollno=i)
    form = StudentModelForm(instance=student)
    if request.method == 'POST':
        form = StudentModelForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('show_stu')
    context = {'form':form}
    template_name = 'InstituteApp/addstudent.html'
    return render(request,template_name,context)


