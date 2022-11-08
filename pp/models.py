from django.db import models
# Register your models here.

class Reviewsss(models.Model):
    name = models.TextField()
    linkedin = models.TextField()
    priority = models.IntegerField(default = 0)
    title = models.TextField()
    review = models.TextField()
    turnonn = models.BooleanField(default = "false")