from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def image_roll_path(instance, filename):   
    return f'user/{instance.role}/institute/{filename}'

class Staff(models.Model):

    ROLE_CHOICES = (
    ("Principal", "Principal"),
    ("Managment Staff", "ManagmentStaff"),
    ("Teacher", "Teacher"),
    ("Accountant", "Accountant"),
    ("Store Manager", "StoreManager"),
    ("Other", "Other"),
    )
    GENDER_CHOICES = (
    ("Male", "male"),
    ("Female", "female"),
    )
    RELIGION_CHOICES = (
    ("Athiest", "Athiest"),
    ("Religion", "religion"),
    )
    BLOOD_CHOICES = (
    ("A", "A"),
    ("A-", "A-"),
    ("B", "B"),
    ("B-", "B-"),
    ("AB", "AB"),
    ("AB-", "AB-"),
    )


    user = models.OneToOneField(User, related_name = 'staff',  on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    phoneNumber = models.PositiveIntegerField(null = True, blank = True)
    role = models.CharField(max_length = 60, choices = ROLE_CHOICES )
    image =  models.ImageField(upload_to = image_roll_path)
    joingDate = models.DateField()
    DateOFBirth = models.DateField()
    monthlySalary = models.PositiveIntegerField()
    fatherHusbandName = models.CharField(max_length = 100 , null = True, blank = True)
    address = models.CharField(max_length = 100 , null = True, blank = True)
    gender = models.CharField(max_length = 6, choices = GENDER_CHOICES, null = True, blank = True)
    religion = models.CharField(max_length = 10, choices = RELIGION_CHOICES, null = True, blank = True)
    experince = models.TextField(null = True, blank = True)
    education = models.TextField(null = True, blank = True)
    nationalID = models.CharField(max_length = 60 , null = True, blank = True)
    emailAddress = models.EmailField(max_length=254,null = True, blank = True)
    bloodGroup = models.CharField(max_length = 3, choices = BLOOD_CHOICES, null = True, blank = True)
    
    def __str__(self):
        return self.name

    


class StaffIDCard(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    issue_date = models.DateField()
    card_number = models.CharField(max_length=50 , unique=True)
    
    def __str__(self):
        return self.staff

class JobLetter(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    issue_date = models.DateField()
    content = models.TextField()
    
    def __str__(self):
        return self.staff
    








# Salary

class Salary(models.Model):
    Months_CHOICES = (
        ("January", "January"),
        ("February", "February"),
        ("March", "March"),
        ("April", "April"),
        ("May", "May"),
        ("June", "June"),
        ("July", "July"),
        ("August", "August"),
        ("September", "September"),
        ("October", "October"),
        ("November", "November"),
        ("December", "December"),
    )
    staff = models.ForeignKey('Staff', related_name='staff_salary', on_delete=models.CASCADE)
    salary_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField()
    salary_month = models.CharField(max_length=20, choices=Months_CHOICES, default="January")  
    any_bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  
    any_deduction = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  

    def __str__(self):
        return f"{self.staff.first_name} {self.staff.last_name} - {self.salary_month}"

# Live Class 


class LiveClass(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    meeting_title = models.CharField(max_length=255, default='')  
    meeting_id = models.CharField(max_length=100, default='')  
    meeting_with_choices = [
        ('All Students' , 'All Students'),
        ('All Teachers' , 'All Teachers'),
        ('Specific Class' , 'Specific Class'),
        ('Specific Student' , 'Specific Student'),
        ('Specific Teacher' , 'Specific Teacher'),
    ]
    meeting_with = models.CharField(max_length=255, choices=meeting_with_choices, default='All Students')
    duration = models.DurationField(default=None) 
    message = models.TextField(default='')  

    def __str__(self):
        return self.meeting_title