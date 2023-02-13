from rest_framework import serializers
from .models import Department, Employee


class Employee_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields ='__all__'

class Department_Serializers(serializers.ModelSerializer):
    maneger_id = Employee_Serializers(read_only=True)
    
    class Meta:
        model = Department
        fields ='__all__'