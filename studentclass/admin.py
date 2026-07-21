from django.contrib import admin
from .models import Class, Subject, HomeWork, ClassTest, TestResult, Behaviour, Skill, DomainRatingReport

class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'Class_name', 'monthly_tution_fee', 'institute', 'Select_Class_Teacher')
    list_filter = ('monthly_tution_fee', 'institute__institute_name', 'Select_Class_Teacher')

admin.site.register(Class, ClassAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Subject, SubjectAdmin)

class HomeWorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'teacher', 'studentClass', 'date')
    list_filter = ('teacher', 'studentClass', 'date')

admin.site.register(HomeWork, HomeWorkAdmin)

class ClassTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_assigned', 'subject', 'date')
    list_filter = ('class_assigned', 'subject', 'date')

admin.site.register(ClassTest, ClassTestAdmin)

class TestResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_test', 'student', 'marks_obtained')
    list_filter = ('class_test__class_assigned', 'student')

admin.site.register(TestResult, TestResultAdmin)

class BehaviourAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'behaviour', 'rating')
    list_filter = ('student', 'behaviour', 'rating')

admin.site.register(Behaviour, BehaviourAdmin)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'skill', 'rating')
    list_filter = ('student', 'skill', 'rating')

admin.site.register(Skill, SkillAdmin)

class DomainRatingReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'domain', 'rating', 'date_generated')
    list_filter = ('student', 'domain', 'rating', 'date_generated')

admin.site.register(DomainRatingReport, DomainRatingReportAdmin)
