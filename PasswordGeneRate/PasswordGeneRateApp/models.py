from django.db import models

# Create your models here.
class Password(models.Model):
    password = models.CharField(max_length = 100, unique = True)

    def __str__(self):
        return self.password
    
class Insult(models.Model):
    insult = models.CharField(max_length = 255, unique = True)

    def __str__(self):
        return self.insult