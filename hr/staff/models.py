from django.db import models

# Create your models here.
class hrdata(models.Model):
    username=models.CharField(("User Name"), max_length=50)
    password=models.CharField(("Password"), max_length=50)
    def __str__(self):
        return self.username