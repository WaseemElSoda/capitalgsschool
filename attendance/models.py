from django.db import models
from student.models import Student
from studentclass.models import Class
from staff.models import Staff

# Create your models here.
class StudentAttendence(models.Model):
    ATTENDENCE_CHOICES = (
        ("P", "P"),
        ("L", "L"),
        ("A", "A"),
    )

    student = models.ForeignKey(Student, related_name='attendence', on_delete=models.CASCADE)
    studentClass = models.ForeignKey(Class, related_name='attendence', on_delete=models.CASCADE)
    date = models.DateField()
    attendence = models.CharField(max_length=1, choices=ATTENDENCE_CHOICES)

    class Meta:
        unique_together = ('student', 'studentClass', 'date')
    
    def __str__(self):
        return self.student.name + " " + self.studentClass.name + " " + str(self.date)
    
    
class StaffAttendence(models.Model):
    ATTENDENCE_CHOICES = (
        ("P", "P"),
        ("L", "L"),
        ("A", "A"),
    )

    staff = models.ForeignKey(Staff, related_name='attendence', on_delete=models.CASCADE)
    date = models.DateField()
    attendence = models.CharField(max_length=1, choices=ATTENDENCE_CHOICES)

    class Meta:
        unique_together = ('staff', 'date')
    
    def __str__(self):
        return self.staff.name + " " + str(self.date)
