from dataclasses import field
from django import forms

level_choices =[('1','1'),('2','2'),('3','3'),('4','4')]
department_choices = [('General','General'),('AI','AI'),('CS','CS'),('IS','IS'),('IT','IT'),('DS','DS')]
status_choices =(('active','active'), ('inactive','inactive'))
gender_choices = (('male','male'),('female','female'))


class updateform(forms.Form):
    id=forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class': 'fff'}))
    name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'fff'}))
    gpa=forms.DecimalField(max_digits=4,decimal_places=2,widget=forms.TextInput(attrs={'class': 'fff'}))
    Email=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'fff'}) )
    phone=forms.CharField(max_length=11,widget=forms.TextInput(attrs={'class': 'fff'}))
    level=forms.ChoiceField(choices= level_choices,widget=forms.Select(attrs={'class': 'fff'}))
    gender=forms.ChoiceField(choices=gender_choices,widget=forms.Select(attrs={'class': 'fff'}))
    department=forms.ChoiceField(choices= department_choices,widget=forms.Select(attrs={'class': 'fff'}))
    status=forms.ChoiceField(choices=status_choices,widget=forms.Select(attrs={'class': 'fff'}))
    date=forms.DateField(widget=forms.DateInput(attrs={'class': 'fff'}))