from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
chooose = (
   (1,'★☆☆☆☆'),
   (2,'★★☆☆☆'),
   (3,'★★★☆☆'),
   (4,'★★★★☆'),
   (5,'★★★★★'),

)

class Movie(models.Model):
    title = models.CharField(max_length=45, unique=True,null=True)
    rating = models.PositiveSmallIntegerField(choices=chooose)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1799),MaxValueValidator(2030),])