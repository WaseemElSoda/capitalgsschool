from django.db import models
from staff.models import Staff
from student.models import Student

# Create your models here.

class Message(models.Model):
    ALL_TEACHERS = 'All Teachers'
    ALL_STUDENTS = 'All Students'
    SPECIFIC_TEACHER = 'Specific Teacher'
    SPECIFIC_STUDENT = 'Specific Student'

    COMMUNICATION_CHOICES = [
        (ALL_TEACHERS, 'All Teachers'),
        (ALL_STUDENTS, 'All Students'),
        (SPECIFIC_TEACHER, 'Specific Teacher'),
        (SPECIFIC_STUDENT, 'Specific Student'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    date_sent = models.DateField()
    communication_type = models.CharField(max_length=20, choices=COMMUNICATION_CHOICES, default=ALL_TEACHERS)

    def __str__(self):
        return f"{self.get_communication_type_display()} - {self.date_sent}"


