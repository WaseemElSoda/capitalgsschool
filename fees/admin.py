from django.contrib import admin
from .models import FeeParticulars, Bank_Fee_Challan, Student_Fee_Challan


@admin.register(FeeParticulars)
class FeeParticularsAdmin(admin.ModelAdmin):
    list_display = ['fee_target', 'monthly_tution_amount', 'admission_amount', 'registeration_amount',
                    'art_material_amount', 'transport_amount', 'books_amount', 'uniform_amount',
                    'fine_amount', 'others_amount', 'previous_balance_amount', 'discount_fee_amount']


@admin.register(Bank_Fee_Challan)
class BankFeeChallanAdmin(admin.ModelAdmin):
    list_display = ['bank_name', 'bank_account_no', 'date_issued', 'due_date']
    list_filter = ['date_issued', 'due_date']


@admin.register(Student_Fee_Challan)
class StudentFeeChallanAdmin(admin.ModelAdmin):
    list_display = ["amount", "date_paid", "fee_month", "due_date", "fine_after_due_date", "bank",
                    "student", "bank_copy", "student_copy", "institute_copy"]
    list_filter = ["amount", "date_paid", "fee_month", "due_date", "student"]

