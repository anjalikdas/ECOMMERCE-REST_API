from django.db.models import fields
from rest_framework import serializers
from .models import Company,Employee
from django.db.models.aggregates import Count


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields = ('id','first_name','last_name','address','Phone_no','email','department','Company') 
    

    def validate_Phone_no(self, data): 
        if Employee.objects.filter(Phone_no=data).exists():
            raise serializers.ValidationError("There is already a user with this phone number,please enter difference value") 
        return data    


class CompanySerializer(serializers.ModelSerializer):
    employee= EmployeeSerializer(many=True)
    class Meta:
        model=Company
        fields = ('id','company_name','address','email','Phone_no','employee')
    
    def create(self,validated_data):
        employee_data=validated_data.pop('employee')
        company=Company.objects.create(**validated_data)
        for employee_data in employee_data:
            Employee.objects.create(company=company,**employee_data)
        return company    

    
    def validate_Phone_no(self, data): 
        if Employee.objects.filter(Phone_no=data).exists():
            raise serializers.ValidationError("There is already a user with this phone number,please enter difference value") 
        return data    
    
class DepartmentSerializer(serializers.ModelSerializer):
    employess=serializers.ReadOnlyField()
    department=serializers.ReadOnlyField()
    count=serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields = ('employess','department','count')

    
   

  