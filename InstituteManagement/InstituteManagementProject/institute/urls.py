from django.urls import path
from . views import AddStudent,AddTeacher,AddDepartment,ShowStudent,ShowTeacher,MixedShowView,ShowDepartment,DeleteStudent,DeleteTeacher,DeleteDepartment,StudentUpdateView,TeacherUpdateView,DepartmentUpdateView

urlpatterns=[
    path('add/',AddStudent.as_view(),name='add_student'),
    path('addteacher/',AddTeacher.as_view(),name='add_teacher'),
    path('adddepartment/',AddDepartment.as_view(),name='add_department'),
    path('show/',ShowStudent.as_view(),name='show_student'),
    path('showteacher/',ShowTeacher.as_view(),name='show_teacher'),
    path('showdepartment/',ShowDepartment.as_view(),name='show_department'),


    path('mix/',MixedShowView.as_view(),name='mixed_view'),

    path('deletestud/<int:id>/',DeleteStudent.as_view(),name='delete'),
    path('deleteteach/<int:id>/',DeleteTeacher.as_view(),name='delete'),
    path('deleteDepart/<int:id>/',DeleteDepartment.as_view(),name='delete'),

    path('updatesstud/<int:id>/',StudentUpdateView.as_view(),name='update_stud'),
    path('updateteach/<int:id>/',TeacherUpdateView.as_view(),name='update_teach'),
    path('updatedept/<int:id>/',DepartmentUpdateView.as_view(),name='update_dept'),
]