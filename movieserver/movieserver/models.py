from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Movies(models.Model):
    MOVIE_TYPE = (("v", "VHS"), ("d", "DVD"), ("s", "Streaming"))
    title = models.CharField(max_length=50, unique=False) 
    format = models.CharField(max_length=32, unique=False, choices=MOVIE_TYPE)
    length = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(500)]) 
    year = models.IntegerField(validators=[MinValueValidator(1800), MaxValueValidator(2100)])
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
