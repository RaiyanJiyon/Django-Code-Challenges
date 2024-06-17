from django import forms

class Registration(forms.Form):
    name = forms.CharField(max_length=100, label="Enter Your Name")
    student_id = forms.IntegerField(required=True, label="Enter Your Student ID")
    course_name = forms.CharField(max_length=100, required=True, label="Enter Your wanted course name")
    course_section = forms.CharField(max_length=100, required=True, label="Enter Your wanted course section")
    email = forms.EmailField(required=False, label="Enter Your wanted email")