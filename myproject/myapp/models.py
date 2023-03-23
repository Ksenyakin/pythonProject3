# myapp/models.py

from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    dob = models.DateField()
    lessons = models.IntegerField()
    first_subscription = models.DateField()
    next_subscription = models.DateField()
    valid_skips = models.IntegerField()
    invalid_skips = models.IntegerField()
    late = models.IntegerField()

    def __str__(self):
        return self.name