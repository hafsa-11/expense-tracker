from django.db import models

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('shopping', 'Shopping'),
        ('food', 'Food'),
        ('home', 'Home'),
        ('transport', 'Transport'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField()

    def __str__(self):
        return self.name
