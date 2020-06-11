from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

#class Student(models.Model):
#    first_name = models.CharField(max_length = 250, null = True)
#    last_name = models.CharField(max_length = 250, null = True)
#    address = models.CharField(max_length = 250, null = True)
#    email_address = models.CharField(max_length = 250, null = True)
#
#    def __str__(self):
#        return self.first_name

class Skill(models.Model):
     skill_name = models.CharField(max_length = 250, null = True)
     skill_slug = models.CharField(max_length = 250, null = True)
     def __str__(self):
        return self.skill_name


class Module(models.Model):
     module_name = models.CharField(max_length = 250, null = True)
     skills = models.ManyToManyField(Skill)
     module_slug = models.CharField(max_length = 250, null = True)
     grade = models.PositiveSmallIntegerField(default=0)

     def __str__(self):
        return self.module_name


class Job(models.Model):
     job_role = models.CharField(max_length = 250, null = True)
     job_slug = models.CharField(max_length = 250, null = True)
     skills = models.ManyToManyField(Skill)
     #modules = models.ManyToManyField(Module)

     def __str__(self):
        return self.job_role

class Recommendation(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     recOne = models.CharField(max_length = 250, null = True)
     recTwo = models.CharField(max_length = 250, null = True)
     recThree = models.CharField(max_length = 250, null = True)
     dateAndTimeOfRec = models.DateTimeField(default=timezone.now)

class AdminRequest(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     firstName = models.CharField(max_length = 250, null = True)
     lastName = models.CharField(max_length = 250, null = True)
     message = models.CharField(max_length = 250, null = True)
     dateAdminRequested = models.DateTimeField(default=timezone.now)

class Message(models.Model):
     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
     message = models.CharField(max_length = 500, null = True)
     dateAndTimeSent = models.DateTimeField(default=timezone.now) # try auto_now_add=True

class Chat(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     messages = models.ManyToManyField(Message)
