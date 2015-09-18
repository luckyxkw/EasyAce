from django.db import models

# Create your models here.
class Subject(models.Model):
    LEVEL = (
        ('P', 'Primary School'),
        ('O', 'O-level'),
        ('A', 'A-level'),
    )
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Education(models.Model):
    LEVEL = (
        ('J', 'Junior college'),
        ('P', 'Polytechnic'),
        ('U', 'University'),
    )
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name

class Tutor(models.Model):
    REGION = (
        ('E', 'East'),
        ('W', 'West'),
        ('C', 'Central'),
        ('N', 'North'),
    )
    TIME = (
        ('M', 'Morning'),
        ('A', 'Afternoon'),
        ('E', 'Evening'),
    )
    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    
    name = models.CharField(max_length=100)
    subject_teach = models.ManyToManyField(Subject)
    education = models.ManyToManyField(Education,through='Graduation')
    
    def __str__(self):
        return self.name


class Graduation(models.Model):
    tutor = models.ForeignKey(Tutor)
    education = models.ForeignKey(Education)
    date = models.DateTimeField('Date of graduation')
    description = models.CharField(max_length=500)
