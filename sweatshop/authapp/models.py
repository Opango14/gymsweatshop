from django.db import models

# Create your models here.
# this file we creates database tables

class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=12)
    description=models.TextField()
    def __str__(self):
        return self.email
    
class Enrollment(models.Model):
    Fullname=models.CharField(max_length=25)
    Email=models.EmailField()
    Gender=models.CharField(max_length=25)
    PhoneNumber=models.CharField(max_length=12)
    DOB=models.DateField(auto_now=False, auto_now_add=False)
    SelectMembershipPlan=models.CharField(max_length=200)
    SelectTrainer=models.CharField(max_length=55)
    Reference=models.CharField(max_length=55)
    Address=models.TextField()
    PaymentStatus=models.CharField(max_length=55,blank=True,null=True)
    Price=models.IntegerField(blank=True,null=True)
    DueDate=models.DateTimeField(blank=True,null=True)
    TimeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.Fullname

class Trainer(models.Model):
    name=models.CharField(max_length=25)
    gender=models.CharField(max_length=25)
    phone=models.CharField(max_length=25)
    salary=models.IntegerField()
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.name

class MembershipPlan(models.Model):
    plan=models.CharField(max_length=185)
    duration=models.IntegerField(default=1)
    price=models.IntegerField()
    def __str__(self):
        return self.plan

class Gallery(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='gallery')
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.id

class Attendance(models.Model):
    SelectDate=models.DateTimeField(auto_now_add=True)
    phonenumber=models.CharField(max_length=15)
    Login=models.CharField(max_length=200)
    Logout=models.CharField(max_length=200)
    SelectWorkout=models.CharField(max_length=200)
    TrainedBy=models.CharField(max_length=200)
    def __str__(self):
        return self.id