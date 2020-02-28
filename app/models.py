from django.db import models

# Create your models here.
class RawData(models.Model):
    Specs = (
        ('Urologist', 'Urologist'),
        ('Gynecologist', 'Gynecologist'),
        ('Neurologist', 'Neurologist'),
        ('Cardiologist','Cardiologist'),
        ('Orthopedic Surgeon','Orthopedic Surgeon'),
        ('Dermatologist','Dermatologist'),
        ('Opthalmologist','Opthalmologist'),
        ('Physiotherapist','Physiotherapist'),
    )
    Complexies = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4','4'),
        ('5 ','5 '),
        
    )
    Patient_ID=models.CharField(max_length=300)
    Consultant=models.CharField(max_length=300)
    Specialization= models.CharField(max_length=300 , choices=Specs)
    Disease= models.CharField(max_length=300)
    Complexity= models.CharField(max_length=300, choices=Complexies)

class Results(models.Model):
    Consultant= models.CharField(max_length=300)
    Specialization= models.CharField(max_length=300)
    Cases=models.CharField(max_length=300)
    Efficiency= models.CharField(max_length=300)


class PharmacyData(models.Model):
    Specialization=models.CharField(max_length=300)
    Disease=models.CharField(max_length=300)
    Medication=models.CharField(max_length=300)
    In_Stock=models.CharField(max_length=300)
    Out_Stock=models.CharField(max_length=300)
