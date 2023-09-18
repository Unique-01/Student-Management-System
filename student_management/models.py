from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Department(models.Model):
    department_code = models.CharField(max_length=10, unique=True)
    department_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.department_name

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    guardian_name = models.CharField(max_length=100)
    guardian_phone_number = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    admission_year = models.PositiveIntegerField()
    matriculation_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    jamb_admission_letter = models.FileField(upload_to='admission_letter')
    birth_certificate = models.FileField(upload_to='birth_certificate',null=True)
    certificate_of_origin = models.FileField(upload_to='certificate_of_origin',null=True)
    status = models.CharField(max_length=50,choices=[('approved','Approved'),('pending','Pendng'),('disapprove','Disapprove')], default='pending')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class MatriculationNumberCounter(models.Model):
    last_generated_number = models.IntegerField(default=0)

