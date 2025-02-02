from django.urls import path
from . import views
urlpatterns = [
    path('employees/', views.get_employees, name='get-employees'),
    path('employees/<int:employee_id>', views.get_employee, name='get-employee'),
    path('employees/create', views.create_employee, name='create-employee'),
    path('employees/update/<int:employee_id>', views.update_employee, name='update-employee'),
    path('employees/delete/<int:employee_id>', views.delete_employee, name='delete-employee'),
]
