# crud/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('departments/', views.DepartmentList.as_view()),
    path('departments/<int:pk>/', views.Department_by_id.as_view()),
    path('departments/delete/<int:pk>', views.DepartmentDelete.as_view()),
    path('departments/update/<int:pk>', views.DepartmentUpdate.as_view()),
    path('employees/', views.EmployeeList.as_view()),
    path('employees/<int:pk>/', views.Employee_by_id.as_view()),
    path('employees/delete/<int:pk>', views.EmployeeDelete.as_view()),
    path('employees/update/<int:pk>', views.EmployeeUpdate.as_view()),
]

