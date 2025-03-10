from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['reg_no', 'department', 'semester', 'division', 'date_of_birth', 'batch', 'phone_no', 'tutor']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Customize form appearance
        self.fields['reg_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['department'].widget.attrs.update({'class': 'form-control'})
        self.fields['semester'].widget.attrs.update({'class': 'form-control'})
        self.fields['division'].widget.attrs.update({'class': 'form-control'})
        self.fields['date_of_birth'].widget.attrs.update({'class': 'form-control'})
        self.fields['batch'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['tutor'].widget.attrs.update({'class': 'form-control'})