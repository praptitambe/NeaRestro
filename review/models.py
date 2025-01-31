from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



STAR_RATINGS = (
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    )

    

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

    def __str__(self):
        return self.name

class Ratings(models.Model):
    rating = models.IntegerField(choices=STAR_RATINGS, default=1)
    restro = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.restro.name} - {self.rating}"
    
    class Meta:
        ordering = ['-rating']

class Comments(models.Model):
    comment = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    restro = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.restro.name} - {self.comment[:20]}"

    class Meta:
        ordering = ['-created_at']
