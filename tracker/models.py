from django.db import models

# Create your models here.

class User(models.Model):
    Pname = models.CharField(max_length=128)
    Cname = models.CharField(max_length=128)

    def __unicode__(self):
        return self.Pname
