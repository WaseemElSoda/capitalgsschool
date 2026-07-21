from django.contrib import admin
from .models import StudentAttendence, StaffAttendence

@admin.register(StudentAttendence)
class StudentAttendenceAdmin(admin.ModelAdmin):
    list_display = ['student', 'studentClass', 'date', 'attendence']
    list_filter = ['studentClass', 'date', 'attendence']

@admin.register(StaffAttendence)
class StaffAttendenceAdmin(admin.ModelAdmin):
    list_display = ['staff', 'date', 'attendence']
    list_filter = ['date', 'attendence']
