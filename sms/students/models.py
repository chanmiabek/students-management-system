from django.db import models

# Create your models here.
class Student(models.Model):
    student_number= models.PositiveBigIntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    field_of_study = models.CharField(max_length=50)
    gpa=models.FloatField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"