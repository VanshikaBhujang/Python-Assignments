from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.BigAutoField(primary_key=True) 
    name = models.CharField(max_length=100)
    salary = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class Department(models.Model):
    dept_id = models.BigAutoField(primary_key=True) 
    name = models.CharField(max_length=100)
    manager_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.department_name