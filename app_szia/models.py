from django.db import models

# Create your models here.

class Teny (models.Model):

    nev = models.CharField(max_length=100)
    ido = models.IntegerField()

    class Meta:
        verbose_name = "Tény"
        verbose_name_plural = "Tények"

    def __str__(self):
        return f'{self.nev} -> {self.ido}'
