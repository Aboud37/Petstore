from django.db import models
from accounts.models import Account
from petshop import settings

class Question(models.Model):
    subject = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(max_length= 5000, blank= False, null= False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank= True, null= True, on_delete=models.CASCADE)

class Response(models.Model):
    question = models.ForeignKey(Question, blank=False, null=False, on_delete=models.CASCADE)
    description = models.TextField(max_length= 5000, blank= False, null= False)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
