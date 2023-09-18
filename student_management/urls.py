from django.urls import path
from . import views

urlpatterns = [
    path('',views.Homepage.as_view(),name='home'),
    path('student-registration/',views.student_registration,name= 'registration'),
    path('staff/dashboard',views.staff_dashboard,name='staff_dashboard'),
    path('staff/student-detail/<id>/',views.student_detail,name='student_detail'),
    path('approve-student/<id>/',views.approve_student,name='approve_student'),
    path('disapprove-student/<id>/',views.disapprove_student,name='disapprove_student'),
    path('generate-matric-number/<id>/',views.generate_matriculation_number, name='generate_matric_number'),
    path('generate-batch-matric-number/',views.generate_batch_matriculation_numbers,name='generate_batch_matric_number'),
    path('export-student-records/',views.export_student_records_as_excel,name='export_student_records'),
]
