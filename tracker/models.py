from django.db import models

# Create your models here.

class User(models.Model):
    Pname = models.CharField(max_length=128, default = "Test")
    Cname = models.CharField(max_length=128, default = "Test")
    UID = models.CharField(max_length=128, default = "Test")
    PicUrl = models.URLField(default = "http://ksmart.herokuapp.com")
    PhoneNumber = models.PositiveIntegerField(default = 0)

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