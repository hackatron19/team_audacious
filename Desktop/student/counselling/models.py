from django.db import models


class Counseling(models.Model):
    email = models.EmailField()
    Qualification = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=20)



