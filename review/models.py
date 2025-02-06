from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


    

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

class Cuisine(models.Model):
    cuisine_type = models.CharField(max_length=140)
    description = models.TextField()

    def __str__(self):
        return self.cuisine_type

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    email = models.EmailField(max_length=255)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=20)
    restro_image = CloudinaryField('image', default='placeholder', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)

    def average_rating(self):
        """Calculate the average rating from comments"""
        avg = self.comments_set.aggregate(Avg('rating'))['rating__avg']
        return round(avg, 1) if avg else None  # Rounds to 1 decimal place or returns None

    def __str__(self):
        return self.name


class Comments(models.Model):
    STAR_RATINGS = (
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    )

    comment = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    restro = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=STAR_RATINGS, null=True, blank=True)  # Optional rating field

    def __str__(self):
        rating_str = f" - Rating: {self.rating}⭐" if self.rating else ""
        return f"{self.restro.name} - {self.comment[:20]}{rating_str}"

    class Meta:
        ordering = ['-created_at']
