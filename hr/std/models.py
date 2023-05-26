from django.db import models

# Create your models here.
class Details(models.Model):
    name=models.CharField(("name"), max_length=50)
    pno=models.CharField(("pno"), max_length=50)
    email=models.CharField(("Email"), max_length=50)
    gender=models.CharField(("Gender"), max_length=50)
    dob=models.CharField(("Dob"), max_length=50)
    mock=models.CharField(("Mock Ratings"), max_length=50)
class Credentials(models.Model):
    username=models.CharField(("Username"), max_length=50)
    password=models.CharField(("Password"), max_length=50)