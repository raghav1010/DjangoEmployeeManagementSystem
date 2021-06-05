from django import forms
from django.db.models import fields
from django.db.models.query import QuerySet  
from .models import Employee, System, Leave
from django.contrib.auth.forms import UserCreationForm
from bootstrap_datepicker_plus import DatePickerInput
from django.contrib.auth.models import User




class EmployeeForm(UserCreationForm):  
    class Meta:  
        model = Employee  
        fields = ['name', 'fathername', 'email','gender','DOB','username','password1','password2'] 
        gender = forms.ChoiceField(choices={('Female','Female'),
                                                    ('Male','Male')})
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'fathername': forms.TextInput(attrs={ 'class': 'form-control' }),
            'DOB':forms.DateInput(attrs={ 'class': 'form-control' })
      }


class SystemForm(UserCreationForm):

    class Meta:
        model =  System 
        fields =['username','email','password1','password2']

class DetailForm(forms.ModelForm):
    class Meta:
        model = Employee 
        fields=['name', 'fathername', 'email','gender','DOB','role','dept']
        


class LeaveForm(forms.ModelForm):
    STATUS= [
        ('Approved','Approved'),
        ('Declined','Declined'),
        ('Wait',"Wait"),
      
    ]
    status = forms.ChoiceField(choices=STATUS,required=False)
    class Meta:
        model = Leave
        fields = ['name','startdate','enddate','status']

        
    
    # def __init__(self,user,*args,**kwargs):
    #     self.user = kwargs.pop('user','')
    #     super(LeaveForm,self).__init__(*args,**kwargs)
    
    # def save(self,*args,**kwargs):
    #     self.instance.user=self.user
    #     super(LeaveForm,self).save(*args,**kwargs)
        