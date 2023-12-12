from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    review_text = models.CharField(max_length=100, blank=True)