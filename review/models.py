from django.db import models
from django.contrib.auth.models import User

STAR_RATINGS = (
        (1, ':star:'),
        (2, ':star::star:'),
        (3, ':star::star::star:'),
        (4, ':star::star::star::star:'),
        (5, ':star::star::star::star::star:'),
    )

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=20)
    images = CloudinaryField('irestaurant_images', default='placeholder', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Cuisine(models.Model):
    cuisine_type = models.CharField(max_length=140)
    description = models.TextField()

    def __str__(self):
        return self.cuisine_type

class Ratings(models.Model):
    rating = models.IntegerField()
    restro = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.restro.name} - {self.ratings}"

class Comments(models.Model):
    comment = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    restro = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.restro.name} - {self.comment[:20]}"