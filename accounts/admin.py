from django.contrib import admin
from .models import RulesRegulations, AccountSettings, ChartOfAccount, Income, Expense, Challan , InstituteProfile


@admin.register(InstituteProfile)
class InstituteAdmin(admin.ModelAdmin):
    list_display = ["id", "institute_name", "phone_number", "website_url", "address", "country"]

    # Ensure 'phone_number' and 'institute_name' are valid attributes or methods in InstituteProfile
    def institute_name(self, obj):
        return obj.institute_name

    def phone_number(self, obj):
        return obj.phone_number


@admin.register(RulesRegulations)
class RulesRegulationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'institute_name', 'description')
    list_filter = ('institute_name',)

@admin.register(AccountSettings)
class AccountSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'time_zone', 'institute', 'user_name', 'currency')
    list_filter = ('time_zone', 'institute', 'currency')

@admin.register(ChartOfAccount)
class ChartOfAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ChartOfAccount_types', 'institute')
    list_filter = ('ChartOfAccount_types', 'institute')

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'description', 'amount')
    list_filter = ('date',)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'description', 'amount')
    list_filter = ('date',)

@admin.register(Challan)
class ChallanAdmin(admin.ModelAdmin):
    list_display = ('id', 'feeMonth', 'date', 'amount', 'fineAfterDueDate', 'bank', 'student')
    list_filter = ('feeMonth', 'date', 'bank', 'student')

