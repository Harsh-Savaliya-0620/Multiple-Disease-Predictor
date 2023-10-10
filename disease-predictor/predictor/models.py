from django.db import models

class Hospital_Name(models.Model):
    Name = models.CharField(max_length=100)
    Location = models.CharField(max_length=60)
    Image = models.ImageField(upload_to="hospital/Images")