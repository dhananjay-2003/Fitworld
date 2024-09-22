from django.db import models
from django.utils import timezone
timezone.now()

from django.http import request




# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    problem = models.TextField()


    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from '+self.firstname


class Appointment(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    request = models.TextField(blank = True)
    phone = models.CharField(max_length=10)
    sent_date = models.DateField( auto_now_add=False,default=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField( auto_now_add=False, null=True, blank=True)
    course = models.CharField(max_length=100, null=True)
    event_time =models.TimeField(auto_now=True, auto_now_add=False)
    request_date =models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering =["-sent_date"]


class Batch_Appointment(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    sent_date = models.DateField( auto_now_add=False,default=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField( auto_now_add=False, null=True, blank=True)
    event_time =models.TimeField(auto_now=True, auto_now_add=False)
    course = models.CharField( max_length=50, null=True)
    request_date =models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Feedback(models.Model):
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.rating)









