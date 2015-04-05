from django.db import models

class Welcome(models.Model):
    text = models.TextField()
    enabled = models.BooleanField(default=True)

class About(models.Model):
    text = models.TextField()
    enabled = models.BooleanField(default=True)
