from myApp.models import Employee
from django import forms
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        field='__all__'
