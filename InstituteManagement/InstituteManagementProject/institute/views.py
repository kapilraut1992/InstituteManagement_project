from django.shortcuts import render,redirect
from . forms import*
from . models import *
from django.views import View


# Create your views here.

class AddStudent(View):
    def get(self, request):
        form = StudentForm()
        template = 'institute/addStudent.html'
        context ={'form': form}
        return render(request, template, context)
    def post(self,request):
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_student')
        template='institute/addStudent.html'
        context={'form':form}
        return render(request,template,context)





class ShowStudent(View):
    def get(self,request):
        student_obj=Student.objects.all()
        template='institute/showStudent.html'
        context={'student_obj':student_obj}
        return render(request,template,context)



class AddTeacher(View):
    def get(self, request):
        form = TeacherForm()
        template='institute/addTeacher.html'
        context ={'form':form}
        return render(request,template,context)

    def post(self,request):
        form=TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_teacher')
        template='institute/addTeacher.html'
        context={'form':form}
        return render(request,template,context)





class ShowTeacher(View):
    def get(self,request):
        teach=Teacher.objects.all()
        template='institute/showteacher.html'
        context={'teach':teach}
        return render(request,template,context)

    




class AddDepartment(View):
    def get(self, request):
        form = DepartmentForm()
        template = 'institute/addDepartment.html'
        context = {'form':form}
        return render(request, template, context)

    def post(self,request):
        form=DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_department')
        template='institute/addDepartment.html'
        context={'form':form}
        return render(request,template,context)




class ShowDepartment(View):
    def get(self,request):
        dept_obj=Department.objects.all()
        template='institute/showdepartment.html'
        context={'dept_obj':dept_obj}
        return render(request,template,context)
    def post(self,request):
        dept_obj=Department.objects.all()

        department=Department.objects.filter(dept_name__icontains=request.POST['searchdata'])
        # print('------', department)
        professor=department[0].department_pro.all()
        print('@@@@@@@@@@@@', professor)
        student=department[0].department_stud.all()
        print('$$$$$$$$$$$$$', student)
        template_name='institute/MixedView.html'
        context={'department':department,'professor':professor,'student':student}
        return render(request,template_name,context)

    # template_name = "DepartmentApp/showDepartment.html"
    # context = {'dept_Obj': dept_obj}
    # return render(request, template_name, context)







class MixedShowView(View):
    def get(self,request):
        teach=Teacher.objects.all()
        a={'teach':teach}
        stud=Student.objects.all()
        b={'stud':stud}

        dept_obj=Department.objects.all()
        c={'dept_obj':dept_obj}

        template='institute/MixedView.html'
        context=((a|b|c))


        return render(request, template, context)


class StudentUpdateView(View):
    def get(self,request,id):
        stud=Student.objects.get(id=id)
        form=StudentForm(instance=stud)
        template='institute/addStudent.html'
        context={'form':form}
        return render(request,template,context)

    def post(self,request,id):
        stud=Student.objects.get(id=id)
        form=StudentForm(request.POST,instance=stud)
        if form.is_valid():
            form.save()
            return redirect('show_student')
        template='institute/addStudent.html'
        context={"form":form}
        return render(request,template,context)


class TeacherUpdateView(View):
    def get(self, request, id):
        teach = Teacher.objects.get(id=id)
        form = TeacherForm(instance=teach)
        template = 'institute/addTeacher.html'
        context = {'form': form}
        return render(request, template, context)

    def post(self, request, id):
        teach = Teacher.objects.get(id=id)
        form = TeacherForm(request.POST, instance=teach)
        if form.is_valid():
            form.save()
            return redirect('show_teacher')
        template = 'institute/addTeacher.html'
        context = {"form": form}
        return render(request, template, context)


class DepartmentUpdateView(View):
    def get(self, request, id):
        depart = Department.objects.get(id=id)
        form = DepartmentForm(instance=depart)
        template = 'institute/addDepartment.html'
        context = {'form': form}
        return render(request, template, context)

    def post(self, request, id):
        depart = Department.objects.get(id=id)
        form = DepartmentForm(request.POST, instance=depart)
        if form.is_valid():
            form.save()
            return redirect('show_department')
        template = 'institute/addDepartment.html'
        context = {"form": form}
        return render(request, template, context)




class DeleteStudent(View):
    def get(self,request,id):
        stud=Student.objects.get(id=id)
        template='institute/confirm_delete.html'
        context={'stud':stud}
        return render(request,template,context)

    def post(self,request,id):
        stud = Student.objects.get(id=id)
        stud.delete()
        return redirect('show_student')




class DeleteTeacher(View):
    def get(self,request,id):
        teach=Teacher.objects.get(id=id)
        template='institute/confirm_delete_teacher.html'
        context={'teach':teach}
        return render(request,template,context)

    def post(self,request,id):
        teach = Teacher.objects.get(id=id)
        teach.delete()
        return redirect('show_teacher')



class DeleteDepartment(View):
    def get(self,request,id):
        depart = Department.objects.get(id=id)
        template='institute/confirm_delete_department.html'
        context={'depart':depart}
        return render(request,template,context)

    def post(self,request,id):
        depart = Department.objects.get(id=id)
        depart.delete()
        return redirect('show_department')

#
# def searchBarView(request):
#     if request.method=="POST":
