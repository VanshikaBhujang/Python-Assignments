from rest_framework import generics


from .models import Employee, Department
from .serializers import Employee_Serializers, Department_Serializers

class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = Department_Serializers

class DepartmentUpdate(generics.UpdateAPIView):
    serializer_class = Department_Serializers
    queryset = Department.objects.all()
    allowed_methods = ['put']

    def get_object(self):
        return Department.objects.get(pk=self.kwargs['pk'])

class DepartmentDelete(generics.DestroyAPIView):
    queryset = Department.objects.all()
    allowed_methods = ['delete']
    
    def get_object(self):
        return Department.objects.get(pk=self.kwargs['pk'])

class Department_by_id(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = Department_Serializers



class EmployeeUpdate(generics.UpdateAPIView):
    serializer_class = Employee_Serializers
    queryset = Employee.objects.all()
    allowed_methods = ['put']

    def get_object(self):
        return Employee.objects.get(pk=self.kwargs['pk'])

class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = Employee_Serializers

class Employee_by_id(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = Employee_Serializers

class EmployeeDelete(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    allowed_methods = ['delete']

    def get_object(self):
        return Employee.objects.get(pk=self.kwargs['pk'])
