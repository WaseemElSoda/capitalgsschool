from django.contrib import admin
from .models import Staff, StaffIDCard, JobLetter, Salary, LiveClass


# Register your models here.

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ["id", "phoneNumber", "name", "role"]
    list_filter = ["role"]

@admin.register(StaffIDCard)
class StaffIDCardAdmin(admin.ModelAdmin):
    list_display = ["staff", "issue_date", "card_number"]
    list_filter = ["issue_date"]

@admin.register(JobLetter)
class JobLetterAdmin(admin.ModelAdmin):
    list_display = ["staff", "issue_date"]
    list_filter = ["issue_date"]

@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ["staff", "salary_amount", "date_paid", "salary_month"]
    list_filter = ["date_paid", "salary_month"]

@admin.register(LiveClass)
class LiveClassAdmin(admin.ModelAdmin):
    list_display = ["meeting_title", "date", "start_time", "end_time", "meeting_with"]
    list_filter = ["date", "meeting_with"]
