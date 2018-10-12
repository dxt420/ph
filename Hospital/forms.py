from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from . models import CustomUser

from django.forms import ModelChoiceField,ModelForm,TextInput,Textarea

from . choices import GENDER_CHOICES,BLOOD_GROUPS,PAYMENT_STATUS,BED_TYPES,MONTHS,YEAR_CHOICES,PAYMENT_STATUS

from django.db import transaction

from django.utils.translation import ugettext_lazy as _
import datetime




class CustomUserCreationForm(UserCreationForm):
    USER_TYPE_CHOICES = (
        (1,'admin'),
        (2,'doctor'),
    )
    user_type =forms.ChoiceField(choices=USER_TYPE_CHOICES,
        widget=forms.Select(attrs={'class' : 'form-control'}))
    name =  forms.CharField(max_length=30)
    dob = forms.DateField()
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','email')

# class CustomUserCreationFormDoctor(UserCreationForm):
#     dob = forms.CharField(max_length=30,
#         widget=forms.TextInput(attrs={'class' : 'form-control datepicker','autocomplete':'off'}))
#     departmentname = forms.ModelChoiceField(queryset=Department.objects.all(), to_field_name="departmentname",
#         widget=forms.Select(attrs={'class' : 'form-control'}))
#     username = forms.CharField(max_length=30,
#         widget=forms.TextInput(attrs={'class' : 'form-control','autocomplete':'off'}))
#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={'class' : 'form-control'}))
#     first_name = forms.CharField(max_length=30,
#         widget=forms.TextInput(attrs={'class' : 'form-control','autocomplete':'off'}))
#     last_name = forms.CharField(max_length=30,
#         widget=forms.TextInput(attrs={'class' : 'form-control','autocomplete':'off'}))
#     phone = forms.CharField(max_length=30,
#         widget=forms.TextInput(attrs={'class' : 'form-control','autocomplete':'off'})) 
#     password1 = forms.CharField(max_length=30,
#         widget=forms.TextInput(attrs={'class' : 'form-control','type' : 'password',}))   
#     password2 = forms.CharField(max_length=30,
#         widget=forms.TextInput(attrs={'class' : 'form-control','type' : 'password',}))  


#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#         fields = ('first_name','last_name','email','username','phone')
        
#     def __init__(self, *args, **kwargs):
#         super(CustomUserCreationFormDoctor, self).__init__(*args, **kwargs)
#         self.fields['email'].label = "Email Address"
#         self.fields['password1'].label = "Password"
#         self.fields['password2'].label = "Re-Type Password"
#         self.fields['dob'].label = "Date of Birth"

#     @transaction.atomic    
#     def save(self):        
#         user = super().save(commit=False)
#         user.is_doctor = True
        

#         user.save()    
        


#         # user.role.set(range(Role.DOCTOR))     
#         doctor = Doctor.objects.create(user=user)  
#         Employee.objects.create(user=user)  
#         # doctor.departmentname.add(*self.get('departmentname'))    
#         # doctor.usericon.add(*self.get('usericon'))    
            
#         return doctor

