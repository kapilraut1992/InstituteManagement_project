from django.db import models

# Create your models here.


class Department(models.Model):
    dept_name = models.CharField(max_length=50,unique=True)
    intake=models.IntegerField()

    def __str__(self):
        return self.dept_name


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=50)
    salary=models.IntegerField()
    dept = models.ManyToManyField(Department, related_name='department_pro')

    def __str__(self):
        return f"{self.teacher_name},{self.dept}"


class Student(models.Model):
    stud_name = models.CharField(max_length=50)
    stud_roll = models.IntegerField()
    stud_marks = models.FloatField()
    dept = models.ForeignKey(Department,related_name='department_stud',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.stud_name},{self.stud_roll},{self.stud_marks},{self.dept}"


