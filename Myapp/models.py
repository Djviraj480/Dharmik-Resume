from django.db import models

# Create your models here.

class Contacts(models.Model):
    yourname                  = models.CharField(max_length=100)
    youremail                 = models.EmailField(max_length=100)
    subject                   = models.CharField(max_length=100)
    massage                   = models.TextField()

    def __str__(self):
    	 return self.yourname + "  " + self.subject + " ------------------------------------------------> " + self.youremail