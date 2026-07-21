from django.db import models
from django.contrib.auth.models import User
from myapp.models import Bank ,InstituteProfile




    


class RulesRegulations(models.Model):
    institute_name = models.ForeignKey(InstituteProfile,related_name="rules_regulations", on_delete=models.CASCADE)
    description = models.TextField()
    
    def __str__(self):
        return self.institute_name
    
    
class AccountSettings(models.Model):
    TIME_ZONE_CHOICES = [
        ('Asia/Karachi', 'Asia/Karachi'),
        ('Asia/Dehli', 'Asia/Dehli'),
    ]

    CURRENCY_CHOICES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('GBP', 'British Pound'),
        # Add more currency choices as needed
    ]

    time_zone = models.CharField(max_length=50, choices=TIME_ZONE_CHOICES, default='Asia/Karachi')
    institute = models.ForeignKey(InstituteProfile, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=250, default="")
    password = models.IntegerField( default='password')
    currency = models.CharField(max_length=200, choices=CURRENCY_CHOICES, default='USD')

    def __str__(self):
        return str(self.institute)


# Accounts 
class ChartOfAccount(models.Model):
    TYPE_CHOICES = [
        ('Type', 'Type'),
        ('Income', 'Income'),
        ('Expense', 'Expense'),
    ]

    institute = models.ForeignKey(InstituteProfile,related_name="institute", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    ChartOfAccount_types = models.CharField(max_length=7, choices=TYPE_CHOICES, default='Type')

    def __str__(self):
        return self.name  

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    date = models.DateField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.description[:20]} - ${self.amount}"
    
    
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    date = models.DateField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.description[:20]} - ${self.amount}"
    
    

class Challan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    description = models.TextField()
    feeMonth = models.DateField()
    date = models.DateField()
    amount = models.PositiveIntegerField()
    fineAfterDueDate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    bank = models.OneToOneField(Bank, related_name="Challans_generated", on_delete=models.CASCADE)
    student = models.OneToOneField('student.Student', related_name="challans", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.description[:20]} - ${self.amount}"