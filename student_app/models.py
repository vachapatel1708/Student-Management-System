from django.db import models

# Create your models here.

class Student(models.Model):

    gender = (
        ('male','male'),
        ('female','female')
    )

    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10,choices=gender)
    phone = models.IntegerField()
    city = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    fees = models.FloatField()
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name
    
class Payment(models.Model):

    method = (
        ('cash', 'cash'),
        ('online', 'online'),
        ('card', 'card')
    )

    name = models.ForeignKey(Student, on_delete=models.CASCADE)
    payment_amount = models.FloatField()
    date = models.DateField()
    taken_by = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50, choices=method)

    def __str__(self):
        return self.name.name
    