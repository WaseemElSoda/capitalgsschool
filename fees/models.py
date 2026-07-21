from django.db import models
from accounts.models import ChartOfAccount













class FeeParticulars(models.Model):
    All_students_choices = [
        ('all', 'All Students'),
        ('class', 'Specific Class'),
        ('student', 'Specific Student'),
    ]
    fee_target = models.CharField(max_length=10, choices=All_students_choices)
    monthly_tution_fee = models.PositiveIntegerField(default=0)
    monthly_tution_amount = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    admission_fee = models.PositiveIntegerField(default=0)
    admission_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    registeration_fee = models.PositiveIntegerField(default=0)
    registeration_amount = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    art_material = models.CharField(max_length=255, default='')
    art_material_amount = models.DecimalField(max_digits=10, decimal_places=1, default=0)   
    transport = models.CharField(max_length=255, default='')
    transport_amount = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    books = models.CharField(max_length=255, default='')
    books_amount = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    uniform = models.CharField(max_length=255, default='')
    uniform_amount = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    fine = models.CharField(max_length=255, default='')
    fine_amount = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    others = models.CharField(max_length=255, default='')
    others_amount = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    previous_balance = models.CharField(max_length=255, default='')
    previous_balance_amount = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    discount_in_fee = models.CharField(max_length=255, default='')
    discount_fee_amount = models.DecimalField(max_digits=10, decimal_places=1, default=0)

    def __str__(self):
        return f"Fee Particulars for {self.fee_target}"


class Bank_Fee_Challan(models.Model):
    bank_name = models.CharField(max_length=200, default='')  
    bank_address = models.CharField(max_length=500, default='')
    bank_account_no = models.IntegerField(default=0,unique=True)
    date_issued = models.DateField()
    due_date = models.DateField()
    
    def __str__(self):
        return self.bank_name


class Student_Fee_Challan(models.Model):
    chart_of_account = models.ForeignKey(ChartOfAccount, on_delete=models.CASCADE, related_name='student_fee_challans')
    particulars = models.ManyToManyField(FeeParticulars, related_name='student_fee_challans')
    amount = models.PositiveIntegerField( )
    date_paid = models.DateField()
    fee_month = models.CharField(max_length=50)
    due_date = models.DateField()
    fine_after_due_date = models.PositiveIntegerField()
    bank = models.ForeignKey(Bank_Fee_Challan, on_delete=models.CASCADE, related_name='student_fee_challans')
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE, related_name='student_fee_challans')

    # Checkboxes
    bank_copy = models.BooleanField(default=False)
    student_copy = models.BooleanField(default=False)
    institute_copy = models.BooleanField(default=False)

    def __str__(self):
        return f"Challan for {self.student} - {self.fee_month}"
