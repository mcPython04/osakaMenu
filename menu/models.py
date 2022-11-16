from django.db import models


# Create your models here.
class Roll(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    special = models.BooleanField(default=False)
    combo = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class SushiSashimi(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Appetizer(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField(default=0)
    kitchen = models.BooleanField(default=False)    # Default is sushi

    def __str__(self):
        return self.name


class Soup(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Salad(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


class HibachiLunch(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


class HibachiDinner(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


class HibachiKid(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Noodle(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


class FriedRice(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


class SushiDinner(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField(default=0)
    description = models.TextField(default='')

    def __str__(self):
        return self.name


class BentoBox(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


class KitchenDinner(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Dessert(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name
