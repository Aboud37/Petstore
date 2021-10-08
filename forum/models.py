from django.db import models
from accounts.models import Account
from petshop import settings

class Response(models.Model):
    description = models.TextField(max_length= 5000, blank= False, null= False)
    name = models.CharField(blank= True, null= False, max_length= 50)


class Question(models.Model):
    subject = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(max_length= 5000, blank= False, null= False)
    name = models.CharField(blank= True, null= False, max_length= 50)
    response = models.ForeignKey(Response, blank=True, null=True, on_delete=models.CASCADE)






