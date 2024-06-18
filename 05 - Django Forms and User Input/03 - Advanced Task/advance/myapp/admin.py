# myapp/admin.py
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_id', 'gender', 'birth_date', 'email', 'address', 'phone_number')
