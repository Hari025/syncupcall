from django.db import models
class Truecomp(models.Model):
    TC=models.TextField()
    title= models.CharField(max_length=300)
    content= models.TextField()
    attendees= models.TextField()
    date=models.DateField()


class Smart(models.Model):
    TC=models.TextField()
    title= models.CharField(max_length=300)
    content= models.TextField()
    attendees= models.TextField()
    date=models.DateField()

class PDB(models.Model):
    TC=models.TextField()
    title= models.CharField(max_length=300)
    content= models.TextField()
    attendees= models.TextField()
    date=models.DateField()
class DMS(models.Model):
    TC=models.TextField()
    title= models.CharField(max_length=300)
    content= models.TextField()
    attendees= models.TextField()
    date=models.DateField()