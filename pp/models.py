from django.db import models

# Create your models here.
class Reviewsss(models.Model):
    name = models.CharField(max_length = 30, null = False)
    linkedin = models.CharField(max_length = 30, default = "NULL")
    title = models.CharField(max_length = 50, null = False,default = "title")
    review = models.TextField()
    priority = models.IntegerField(default = 0,null=True)
    turnonn = models.BooleanField(default = "false",null=False)


class LetsTalk(models.Model):
    name = models.CharField(max_length = 30)
    company_name= models.CharField(max_length = 60)
    company_email = models.CharField(max_length = 30)
    message = models.TextField() 
