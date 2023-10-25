from django.db import models

class Message(models.Model):
	contenu = models.CharField(max_length=255,default=None,null=True)
# Create your models here.
