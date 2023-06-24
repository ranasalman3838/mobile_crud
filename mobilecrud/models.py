from django.db import models

# Create your models here.

class Mobile(models.Model):
    name = models.CharField(max_length=120)
    company_name = models.CharField(max_length=130)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name + self.company_name
