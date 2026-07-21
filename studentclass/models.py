from django.db import models
from django.core.exceptions import ValidationError
from myapp.models import InstituteProfile  # Assuming InstituteProfile model exists
from staff.models import Staff  # Assuming Staff model exists
from student.models import Student  # Assuming Student model exists

class Class(models.Model):
    Class_name = models.CharField(max_length=255, default="")
    monthly_tution_fee = models.PositiveIntegerField(default=0)
    Class_teacher_CHOICES = [
        ('irfan', 'irfan'),
        ('abbas', 'abbas'),
        ('bilal', 'bilal'),
        # Add more choices as needed
    ]
    institute = models.ForeignKey(InstituteProfile, on_delete=models.CASCADE, default=1)  # Assuming '1' is the ID of your default InstituteProfile
    Select_Class_Teacher = models.ForeignKey(Staff, related_name='classes_taught', on_delete=models.CASCADE, default='irfan')

    def __str__(self):
        return self.Class_name


class Subject(models.Model):
    name = models.CharField(max_length=255)
    classes = models.ManyToManyField(Class, related_name='subjects')

    def __str__(self):
        return self.name


class HomeWork(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Staff, related_name="homeworks_assigned", on_delete=models.CASCADE)
    studentClass = models.ForeignKey(Class, related_name="homeworks_set", on_delete=models.CASCADE)
    date = models.DateField()

    def clean(self):
        if self.teacher.role != "Teacher":
            raise ValidationError(f"The assigned staff must have the role 'Teacher'. Current role: {self.teacher.role}")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.teacher}"


class ClassTest(models.Model):
    class_assigned = models.ForeignKey(Class, related_name="class_tests", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.class_assigned)


class TestResult(models.Model):
    class_test = models.ForeignKey(ClassTest, related_name="test_results", on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()

    def __str__(self):
        return str(self.class_test)


class Behaviour(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="behaviours")
    behaviour = models.CharField(max_length=255)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.student.Student_name} - {self.behaviour}"


class Skill(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="skills")
    skill = models.CharField(max_length=255)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.student.Student_name} - {self.skill}"



class DomainRatingReport(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    domain = models.CharField(max_length=50)
    rating = models.IntegerField()
    date_generated = models.DateField()
    def __str__(self):
        return f"{self.student.Student_name} - {self.domain}"