from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=70)
    image = models.ImageField(default="default_image.jpg", upload_to='images/')
    text = models.TextField()
    likes = models.IntegerField(blank=True)
    rating = models.FloatField(blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)