from django.db import models


# Create your models here.
class Sushi(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    special = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Appetizers(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Hibachi(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Kitchen(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name

