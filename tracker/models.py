from django.db import models

# Create your models here.

class User(models.Model):
    Pname = models.CharField(max_length=128)
    Cname = models.CharField(max_length=128)
    UID = models.CharField(max_length=128)
    PicUrl = models.URLField()
    PhoneNumber = models.PositiveIntegerField(max_length=10)

    def __str__(self):
        return self.UID

class Goal(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class SubGoal(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name