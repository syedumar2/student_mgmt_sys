from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    field_of_study = models.CharField(max_length=100)
    usn = models.CharField(max_length=100, unique=True)
    gpa = models.DecimalField(max_digits=4, decimal_places=2)
    RESULT_CHOICES = [
        ('pass', 'Pass'),
        ('fail', 'Fail'),
    ]
    result = models.CharField(max_length=4, choices=RESULT_CHOICES, default='pass')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.usn})"
