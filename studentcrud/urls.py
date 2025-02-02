from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-student/', views.add_student, name='add-student'),
    path('student-details/<int:student_id>', views.student_details, name='student-details'),
    path('student-update/<int:student_id>', views.update_student, name='student-update'),
    path('delete-student/<int:student_id>', views.delete_student, name='delete-student'),
]
