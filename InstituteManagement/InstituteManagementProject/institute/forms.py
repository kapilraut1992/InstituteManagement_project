from django import forms
from .models import*


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

