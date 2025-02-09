from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

"""
About model - to store information about the site owner
"""
class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    profile_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title
    
class CollaborateRequest(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField()
    restro_name = models.CharField(max_length=200)
    description = models.TextField()
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=20)
    cuisine_type = models.CharField(max_length=140)
    restro_image = CloudinaryField('collaboration_image', default='placeholder')
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Collaboration request from {self.name} for {self.restro_name}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Collaboration Request'
        verbose_name_plural = 'Collaboration Requests'
