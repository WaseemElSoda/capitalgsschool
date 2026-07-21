from django.contrib import admin
from .models import  Bank, GradingSystem, Grade, FailCriteria


# Register your models here.



@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ["id", "name" ,"address"]
    list_filter = ["user"]


class GradeInLine(admin.TabularInline):
    model = Grade
    raw_id_fields = ['gradingSystem']



@admin.register(GradingSystem)
class GradingSystemAdmin(admin.ModelAdmin):
    list_display = ['id']
    inlines = [GradeInLine]



@admin.register(FailCriteria)
class FailCriteriaAdmin(admin.ModelAdmin):
    list_display = ["id", "gradingSystem", "overAllPercentage", "subjectAllPercentage", "noSubject"]







