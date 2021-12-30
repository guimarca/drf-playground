from django.db import models


class Stuff(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField()
