from django.db import models

# Create your models here.
class Reviewsss(models.Model):
    name = models.TextField(null = False)
    linkedin = models.TextField(default = "NULL")
    title = models.TextField(null = False)
    review = models.TextField()
    priority = models.IntegerField(default = 0,null=True)
    turnonn = models.BooleanField(default = "false",null=False)