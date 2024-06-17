from django import forms

class StudentForm(forms.Form):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]
    
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Full Name'})
    )
    
    student_id = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Student ID'})
    )
    
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        required=False,
        widget=forms.RadioSelect
    )
    
    birth_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'type': 'date'})
    )
    
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address'})
    )
    
    address = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Home Address', 'rows': 3})
    )
    
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Phone Number'})
    )
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        return phone_number
