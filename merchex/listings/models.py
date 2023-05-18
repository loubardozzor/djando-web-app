from django.db import models
from django.core.validators import MaxValueValidator,  MinValueValidator
class Band(models.Model):
    def __str__(self):
        return f'{self.name}'
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        MBOLE = 'MB'
        MAKOSSA = 'MA'
        BIKOUSSI = 'BI'
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

class Listing(models.Model):
    class Type(models.TextChoices):
        disques = 'Records'
        vetement = 'Clothing'
        affiches = 'Posters'
        divers = 'Miscellaneous'
    title = models.fields.CharField(max_length=100, default='')
    type  = models.fields.CharField(choices=Type.choices, max_length=20, default='Records')
    description = models.fields.CharField(max_length=100, default='')
    sold = models.fields.BooleanField(default=True)
    year = models.fields.IntegerField(null=True, blank=True)





# Create your models here.
