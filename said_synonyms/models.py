from django.db import models


class SaidSynonym (models.Model):
    term = models.CharField(max_length=255)

    class Meta: 
        ordering = [ 'term' ]

    def __str__ (self):
        return self.term

# Create your models here.
class Category (models.Model):
    name  = models.CharField(max_length=255)
    terms = models.ManyToManyField(SaidSynonym)

    class Meta:
        ordering = [ 'name' ]

    def __str__ (self):
        return self.name
