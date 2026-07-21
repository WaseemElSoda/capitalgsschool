from django.contrib import admin
from .models import Student, AdmissionLetter, StudentIDCard


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "registration", "studentClass", "discountPercentage"]
    list_filter = ["studentClass", "discountPercentage", "prevSchoolName", "religion", "bloodGroup", "orphanStatus"]


@admin.register(AdmissionLetter)
class AdmissionLetterAdmin(admin.ModelAdmin):
    list_display = ["id", "student_name", "student_registration", "student_class", "student_discount_percentage", "issue_date"]
    list_filter = ["student__studentClass", "student__discountPercentage", "student__prevSchoolName", "student__religion", "student__bloodGroup", "student__orphanStatus"]

    def student_name(self, obj):
        return obj.student.name

    def student_registration(self, obj):
        return obj.student.registration

    def student_class(self, obj):
        return obj.student.studentClass.name

    def student_discount_percentage(self, obj):
        return obj.student.discountPercentage


@admin.register(StudentIDCard)
class StudentIDCardAdmin(admin.ModelAdmin):
    list_display = ["id", "student_name", "student_registration", "student_class", "student_discount_percentage", "issue_date", "card_number"]
    list_filter = ["student__studentClass", "student__discountPercentage", "student__prevSchoolName", "student__religion", "student__bloodGroup", "student__orphanStatus"]

    def student_name(self, obj):
        return obj.student.name

    def student_registration(self, obj):
        return obj.student.registration

    def student_class(self, obj):
        return obj.student.studentClass.name

    def student_discount_percentage(self, obj):
        return obj.student.discountPercentage
