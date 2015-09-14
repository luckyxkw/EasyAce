from django.db import models

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=100)
    level = (
        ('P', 'Primary School'),
        ('O', 'O-level'),
        ('A', 'A-level'),
    )
    def __str__(self):
        return self.title

class Education(models.Model):
    name = models.CharField(max_length=100)
    level = (
        ('J', 'Junior college'),
        ('P', 'Polytechnic'),
        ('U', 'University'),
    )

    def __str__(self):
        return self.name

class Tutor(models.Model):
    name = models.CharField(max_length=100)
    gender = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    subject_teach = models.ManyToManyField(Subject)
    education = models.ManyToManyField(Education,through='Graduation')
    region = (
        ('E', 'East'),
        ('W', 'West'),
        ('C', 'Central'),
        ('N', 'North'),
    )
    time = (
        ('M', 'Morning'),
        ('A', 'Afternoon'),
        ('E', 'Evening'),
    )

    def __str__(self):
        return self.name


class Graduation(models.Model):
    tutor = models.ForeignKey(Tutor)
    education = models.ForeignKey(Education)
    date = models.DateTimeField('Date of graduation')
    description = models.CharField(max_length=500)
