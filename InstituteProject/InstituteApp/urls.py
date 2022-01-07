from django.urls import path
from . import views

urlpatterns = [
    path('adddept/',views.adddepartmentmodel,name='add_dept'),
    path('showdept/',views.showdepartment,name='show_dept'),
    path('update1/<int:i>/',views.updatedepartment,name='update_dept'),
    path('delete1/<int:i>/', views.deletedepartment, name='delete_dept'),
    path('addprof/',views.addprofessormodel,name='add_prof'),
    path('showprof/',views.showprofessor,name='show_prof'),
    path('upd/<str:i>/',views.updateprofessor,name='update_prof'),
    path('del/<str:i>/',views.deleteprofessor,name='delete_prof'),
    path('addstu/',views.addstudentmodel,name='add_stu'),
    path('showstu/',views.showstudent,name='show_stu'),
    path('update/<int:i>/',views.updatestudent,name='update_stu'),
    path('delete/<int:i>/',views.deletestudent,name='delete_stu'),
]