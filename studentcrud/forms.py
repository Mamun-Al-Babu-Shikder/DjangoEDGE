from django import forms

from studentcrud.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'cgpa', 'department']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'minlength': 5, 'maxlength': 50}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'minvalue': 15, 'maxvalue': 70}),
            'cgpa': forms.NumberInput(attrs={'class': 'form-control', 'minvalue': 0, 'maxvalue': 4, 'step': 0.01}),
            'department': forms.Select(attrs={'class': 'form-control'}),
        }


