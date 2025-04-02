from django import forms
from .models import Student,Tutor, PlacementOffer,User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "regno", "role"]  # Added first_name & last_name
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "regno": forms.TextInput(attrs={"class": "form-control", "readonly": "readonly"}),  # Read-only
            "role": forms.Select(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

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
        self.fields['reg_no'].widget.attrs.update({'readonly': 'true'})  # Readonly input
        self.fields['department'].widget.attrs.update({'class': 'form-control'})
        self.fields['semester'].widget.attrs.update({'class': 'form-control'})
        self.fields['division'].widget.attrs.update({'class': 'form-control'})
        self.fields['date_of_birth'].widget.attrs.update({'class': 'form-control'})
        self.fields['batch'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['tutor'].widget.attrs.update({'class': 'form-control'})
        

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['tutor_name', 'department', 'semester', 'division']
        widgets = {
            'tutor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Tutor Name'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Department'}),
            'semester': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 8}),
            'division': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Division'}),
        }
        

class PlacementOfferForm(forms.ModelForm):
    class Meta:
        model = PlacementOffer
        fields = [
            "company_name",
            "cgpa_required",
            "no_of_backpapers",
            "salary",
            "description",
            "skillset",
            "contact_email",
            "posted_date",
            "final_date",
            "department",
            "sem"
        ]
        widgets = {
            "posted_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "final_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "skillset": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})