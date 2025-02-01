from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['usn', 'first_name', 'last_name', 'email', 'field_of_study', 'gpa', 'result']
        labels = {
            'usn': 'USN',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'field_of_study': 'Field of Study',
            'gpa': 'GPA',
            'result': 'Result'
        }
        widgets = {
            'usn': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control'}),
            'result': forms.Select(attrs={'class': 'form-control'}, choices=Student.RESULT_CHOICES),
        }

class StudentSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
