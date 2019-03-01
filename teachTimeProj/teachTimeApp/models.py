from django.db import models
from django.utils import timezone
# Create your models here.


# model for teacher

class Teacher(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# model for teachers time cards

class TimeCard(models.Model):
    school = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    hours = models.DecimalField(max_digits=4, decimal_places=2)
    dateOfWork = models.DateTimeField
    dateofEntry = models.DateTimeField(default=timezone.now)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher

