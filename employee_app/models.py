from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

def validate_image_size(image):
    max_size = 5 * 1024 * 1024
    if image.size > max_size:
        raise ValidationError("image size should be 5MB.")
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, validators=[validate_image_size])

    def __str__(self):
        return self.name