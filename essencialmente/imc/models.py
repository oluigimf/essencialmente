from django.db import models

class Avaliar_IMC(models.Model):
    CPF = models.CharField(max_length=11, primary_key=True, unique=True, null=False, blank=False)
    Nome = models.CharField(max_length=150, null=False, blank=False)
    
    