from django.db import models

# Create your models here.
from urllib.parse import MAX_CACHE_SIZE
from django.db import models
from django.conf import settings

# Create your models here.

RATINGS = (
    (1, "Very Poor"),
    (2, "Poor"),
    (3, "Good"),
    (4, "Very Good"),
    (5, "Excellent"),
)

CATEGORY = (
    ("S", "Supermarket"),
    ("E", "Electronics"),
    ("C", "Computer & Other Accessories"),
    ("P", "Mobile Phone & Accessories"),
)

class Item(models.Model):
    name = models.CharField(max_length= 50)
    real = models.FloatField()
    discount = models.FloatField(blank= True, null = True)
    description = models.TextField()
    bestseller = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    new = models.BooleanField(default= False)
    category = models.CharField(max_length=1, choices = CATEGORY)
    # most popular
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to = "image")
    ratings = models.IntegerField( choices=RATINGS, blank = True, null = True)
    reviews = models.TextField( blank = True, null = True)
    

