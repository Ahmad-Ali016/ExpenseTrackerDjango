from django.contrib.auth.models import User
from django.db import models

from ExpenseTrackerDjango import settings


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Expense(models.Model):
    name = models.CharField(max_length=250)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(
    #     request.user,
    #     on_delete=models.CASCADE,
    #     null=True,  # or False if you want to require user immediately
    #     blank=True,
    #     related_name='expenses'
    # )
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True) # FK
    tags = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)   # Auto create timestamp
    updated_at = models.DateTimeField(auto_now=True)       # Auto update timestamp

    def __str__(self):
        return f"{self.name} - {self.amount} - {self.category} - {self.tags}"

