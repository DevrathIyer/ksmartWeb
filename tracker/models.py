from django.db import models

# Create your models here.

class User(models.Model):
    Pname = models.CharField(max_length=128, default = "Test")
    Cname = models.CharField(max_length=128, default="Test")
    City = models.CharField(max_length=128, default="Test")
    UID = models.CharField(max_length=128, default = "Test")
    Email = models.EmailField(default="")
    PicUrl = models.URLField(default = "http://ksmart.herokuapp.com")
    PhoneNumber = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.UID

class Goal(models.Model):
    name = models.CharField(max_length=128)
    date = models.DateField(default = None)
    User = models.ForeignKey(User, on_delete=models.CASCADE, default = None)

    def __str__(self):
        return self.name


class SubGoal(models.Model):
    name = models.CharField(max_length=128)
    date = models.DateField(default = None)
    Goal = models.ForeignKey(Goal, on_delete=models.CASCADE, default = None)

    def __str__(self):
        return self.name